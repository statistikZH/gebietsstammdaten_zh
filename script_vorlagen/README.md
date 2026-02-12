## Script-Vorlagen

Hier stehen Script-Vorlagen zur Verfügung, um aus den **Gebietsstammdaten** im [Kantonalen Datenkatalog](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich) 
weitere Daten zu generieren.


### 1. Historisierung der Gemeindecodes und -namen

Das R-Script [R/Gemeinden_ZH_HIST.R](R/Gemeinden_ZH_HIST.R) lädt Gebietsstammdaten zu Gemeindemutationen (Namensänderungen und Fusionen)
und den Normdaten der aktuellen Gemeinden. 

Damit wird für jedes Jahr rückwärts vom aktuellen Jahr bis 1990 eine Historisierung erstellt:
- Startpunkt: aktuelle Gemeindecodes und -namen mit dem aktuellem Jahr
- Für jedes frühere Jahr werden Mutationen berücksichtigt, d.h. wenn eine Mutation stattfand, wird rückwärts der alte Gemeindecode/Name übernommen.

Ergebnis:
- Eine vollständige Zeitreihe aller Gemeinden von heute bis 1990, gespeichert als [CSV-Datei](daten/gemeinde_code_jahr.csv).

### 2. Python-Helpers für Gebietsstammdaten ZH

Im Ordner [python/gebietsstammdaten_zh](python/gebietsstammdaten_zh/) stehen Python-Hilfsfunktionen zur Verfügung wie z. B. gemeinde_suchen().
Funktionen können im DryRun-Modus ausgeführt werden. Dabei wird kein API-Call durchgeführt, sondern lediglich die generierte Request-URL zurückgegeben. So lassen sich Abfragen prüfen, bevor sie produktiv ausgeführt werden.

Typische Anwendungsfälle:

- Suche nach Gemeinden über Name oder weitere Parameter
- Automatisierte Abfragen für Analysen oder Datenpipelines
- Nutzung in Jupyter Notebooks für explorative Datenanalysen

Die Installation erfolgt idealerweise in einer virtuellen Umgebung (z. B. mit uv).
Beispiel-Notebook: gebietsstammdaten_demo.ipynb.
