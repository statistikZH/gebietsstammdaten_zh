"""Python helpers for the Gebietsstammdaten ZH API and historization logic.

Ported from:
- api/Beispielabfragen.R
- script_vorlagen/Gemeinden_ZH_HIST.R
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import csv
import json
from pathlib import Path
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://gebietsstammdaten.statistik.zh.ch/api"
DEFAULT_TIMEOUT_S = 30


class ApiError(RuntimeError):
    """Raised when the API returns a non-2xx response."""


@dataclass(frozen=True)
class DryRunRequest:
    method: str
    url: str
    json_body: dict[str, Any] | None = None


def _request_json(
    method: str,
    url: str,
    json_body: dict[str, Any] | None = None,
    timeout_s: int = DEFAULT_TIMEOUT_S,
) -> dict[str, Any] | list[Any]:
    data = None
    headers = {"Accept": "application/json"}

    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = Request(url, data=data, headers=headers, method=method)

    try:
        with urlopen(req, timeout=timeout_s) as resp:
            payload = resp.read().decode("utf-8")
    except HTTPError as exc:
        message = exc.read().decode("utf-8") if exc.fp else str(exc)
        raise ApiError(f"API error {exc.code} for {url}: {message}") from exc
    except URLError as exc:
        raise ApiError(f"API request failed for {url}: {exc}") from exc

    try:
        return json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ApiError(f"Invalid JSON response from {url}: {exc}") from exc


def api_health(
    base_url: str = DEFAULT_BASE_URL,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    dry_run: bool = False,
) -> dict[str, Any] | list[Any] | DryRunRequest:
    """Check the API health endpoint."""

    url = f"{base_url}/health"
    if dry_run:
        return DryRunRequest(method="GET", url=url)
    return _request_json("GET", url, timeout_s=timeout_s)


def gemeinde_suchen(
    name: str,
    base_url: str = DEFAULT_BASE_URL,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    dry_run: bool = False,
    normalize: bool = True,
) -> dict[str, Any] | list[Any] | DryRunRequest:
    """Search a municipality by name.

    Note: the API may return a list directly or a dict with a "treffer" key.
    """

    url = f"{base_url}/gemeinden/gemeindename"
    body = {"name": name}
    if dry_run:
        return DryRunRequest(method="POST", url=url, json_body=body)

    response = _request_json("POST", url, json_body=body, timeout_s=timeout_s)
    if normalize and isinstance(response, dict) and "treffer" in response:
        return response["treffer"]
    return response


def bezirk_mit_gemeinden(
    bezirk_code: int | str,
    base_url: str = DEFAULT_BASE_URL,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    dry_run: bool = False,
) -> dict[str, Any] | list[Any] | DryRunRequest:
    """Fetch a district, including its municipalities."""

    url = f"{base_url}/bezirke/{bezirk_code}"
    if dry_run:
        return DryRunRequest(method="GET", url=url)
    return _request_json("GET", url, timeout_s=timeout_s)


def read_csv_from_url(
    url: str,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    encoding: str = "utf-8",
) -> list[dict[str, str]]:
    """Read a CSV from a URL into a list of dicts."""

    req = Request(url)
    try:
        with urlopen(req, timeout=timeout_s) as resp:
            content = resp.read().decode(encoding)
    except URLError as exc:
        raise RuntimeError(f"Failed to fetch CSV from {url}: {exc}") from exc

    return _read_csv_text(content)


def read_csv_from_path(path: Path, encoding: str = "utf-8") -> list[dict[str, str]]:
    """Read a CSV from disk into a list of dicts."""

    content = path.read_text(encoding=encoding)
    return _read_csv_text(content)


def write_csv_rows(
    rows: Iterable[dict[str, Any]],
    path: Path,
    fieldnames: list[str] | None = None,
    encoding: str = "utf-8",
) -> None:
    """Write rows to a CSV file."""

    rows_list = list(rows)
    if not rows_list:
        raise ValueError("No rows provided to write_csv_rows")

    if fieldnames is None:
        fieldnames = list(rows_list[0].keys())

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding=encoding, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_list)


def build_gemeinde_historisierung(
    gemeinden_aktuell_rows: Iterable[dict[str, Any]],
    gemeindmutationen_rows: Iterable[dict[str, Any]],
    start_year: int = 1990,
    end_year: int | None = None,
    current_year: int | None = None,
) -> list[dict[str, Any]]:
    """Build the historical municipality dataset from current data and mutations."""

    if current_year is None:
        current_year = date.today().year
    if end_year is None:
        end_year = current_year
    if end_year < start_year:
        raise ValueError("end_year must be >= start_year")

    mutations_by_year: dict[int, list[dict[str, Any]]] = {}
    for row in gemeindmutationen_rows:
        mutationsdatum = row.get("mutationsdatum")
        if mutationsdatum is None:
            raise ValueError("Mutation row missing 'mutationsdatum'")
        year = _parse_year(str(mutationsdatum))
        mutations_by_year.setdefault(year, []).append(row)

    result: list[dict[str, Any]] = []

    base_rows = [dict(row) for row in gemeinden_aktuell_rows]
    for row in base_rows:
        row["jahr"] = end_year
        result.append(row)

    prev_year_rows = [dict(row) for row in base_rows]

    for year in range(end_year - 1, start_year - 1, -1):
        tmp = [dict(row) for row in prev_year_rows]
        mutations = mutations_by_year.get(year + 1, [])

        if mutations:
            mutation_map: dict[str, tuple[Any | None, Any | None]] = {}
            for mut in mutations:
                key = _code_key(mut.get("gemeinde_code_neu"))
                mutation_map[key] = (
                    mut.get("gemeinde_code_alt"),
                    mut.get("gemeinde_name_alt"),
                )

            for row in tmp:
                key = _code_key(row.get("gemeinde_code"))
                if key in mutation_map:
                    code_alt, name_alt = mutation_map[key]
                    if code_alt is not None and code_alt != "":
                        row["gemeinde_code"] = code_alt
                    if name_alt is not None and name_alt != "":
                        row["gemeinde_name"] = name_alt

        for row in tmp:
            row["jahr"] = year

        result.extend(tmp)
        prev_year_rows = tmp

    result.sort(
        key=lambda r: (
            -int(r["jahr"]),
            _code_key(r.get("gemeinde_code")),
        )
    )

    return result


def _read_csv_text(content: str) -> list[dict[str, str]]:
    reader = csv.DictReader(content.splitlines())
    return [dict(row) for row in reader]


def _parse_year(value: str) -> int:
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%d.%m.%Y"):
        try:
            return datetime.strptime(value, fmt).year
        except ValueError:
            continue

    try:
        return datetime.fromisoformat(value).year
    except ValueError as exc:
        raise ValueError(f"Unsupported date format: {value}") from exc


def _code_key(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()
