# Gebietsstammdaten ZH – Python Helpers

Python-Hilfsfunktionen für die **Gebietsstammdaten ZH API** und historische Gemeindeaufbereitung.

---

## Installation

1. Virtuelle Umgebung vorbereiten:

```bash
uv install
```
oder 

```bash
pip install uv
```

2. Entwicklungsabhängigkeiten inklusive Jupyter hinzufügen:

```bash
uv add --dev jupyter
```

---

## Jupyter Notebook starten

```bash
uv run jupyter notebook
```

- Öffnet die Notebook-Weboberfläche im Browser.
- Notebooks wie `gebietsstammdaten_demo.ipynb` können geöffnet und ausgeführt werden.

---

## Kurzes Beispiel

```python
from gebietsstammdaten_zh import gemeinde_suchen

# DryRun: zeigt nur die URL, ohne API-Aufruf
dry_run = gemeinde_suchen("Bülach", dry_run=True)
print(dry_run)

# Echte Abfrage
result = gemeinde_suchen("Bülach")
print(result)
```

- DryRun gibt ein `DryRunRequest`-Objekt zurück.
- Mit `dry_run=False` wird die API tatsächlich abgefragt.

---

## Hinweise

- GET-Anfragen nutzen Query-Parameter (`?gemeindename=…`).
- `_request_json` behandelt automatisch GET ohne Body, POST/PUT/PATCH mit JSON-Body.
- Kernel-Optionen im Notebook:
  - **Shift + Enter** → Zelle ausführen und zur nächsten springen
  - **Ctrl + Enter** → Zelle ausführen und bleiben
  - **Kernel → Interrupt / Restart** → Kernel stoppen oder neu starten
