# Gebietsstammdaten ZH – Python Helpers

Python-Hilfsfunktionen für die **Gebietsstammdaten ZH API** und historische Gemeindeaufbereitung.

---

## Installation

1. **uv >= 0.13.4** installieren bzw. aktualisieren und mit `uv --version` prüfen.
   Falls pip zur Installation verwendet wird, muss es zuerst sicher auf
   **pip >= 26.2.2** aktualisiert werden. Die
   [Python-Sicherheitsmeldung zum eMudhra/emSign-Vorfall](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)
   enthält dafür einen Download mit SHA256-Prüfsumme.

2. Im Verzeichnis `code_vorlagen/python` die virtuelle Umgebung inklusive
   der bereits deklarierten Jupyter-Abhängigkeiten synchronisieren:

```bash
uv sync --locked --inexact --python 3.14
```

Die gesperrten Abhängigkeiten unterstützen Python 3.15 noch nicht vollständig.

Die Lockdatei enthält **certifi >= 2026.10.19**; eine uv-Constraint verhindert
ältere Versionen bei erneuter Auflösung. Ein separat in der Umgebung installiertes
pip muss ebenfalls mindestens Version 26.2.2 haben: Es enthält ein eigenes
CA-Bundle und wird durch ein certifi-Update nicht repariert. Nach dem Update
laufende Jupyter-Kernel neu starten. Die Hilfsfunktionen verwenden `urllib` und
damit den Python-/System-Zertifikatsspeicher; auch dieser muss aktuell sein.

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
