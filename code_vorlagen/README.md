## Code-Vorlagen

Hier stehen Code-Vorlagen zur Verfügung, zur Verwendung der [API Gebietsstammdaten](https://gebietsstammdaten.statistik.zh.ch/) und um aus den **Gebietsstammdaten** im [Kantonalen Datenkatalog](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich) 
weitere Daten zu generieren. 

### 1. Verwendung API mit R oder Curl

Unter [api](api) stehen Code-Vorlagen zur Verwendung der API mit R und Curl zur Verfügung. 

### 2. Historisierung der Gemeindecodes und -namen

Das R-Script [R/Gemeinden_ZH_HIST.R](R/Gemeinden_ZH_HIST.R) lädt Gebietsstammdaten zu Gemeindemutationen (Namensänderungen und Fusionen)
und den Normdaten der aktuellen Gemeinden. 

Damit wird für jedes Jahr rückwärts vom aktuellen Jahr bis 1990 eine Historisierung erstellt:
- Startpunkt: aktuelle Gemeindecodes und -namen mit dem aktuellem Jahr
- Für jedes frühere Jahr werden Mutationen berücksichtigt, d.h. wenn eine Mutation stattfand, wird rückwärts der alte Gemeindecode/Name übernommen.

Ergebnis:
- Eine vollständige Zeitreihe aller Gemeinden von heute bis 1990, gespeichert als [CSV-Datei](daten/gemeinde_code_jahr.csv).

### 3. Python-Helpers für Gebietsstammdaten ZH

Im Ordner [python/src/gebietsstammdaten_zh](python/src/gebietsstammdaten_zh/) stehen Python-Hilfsfunktionen zur Verfügung wie z. B. gemeinde_suchen().

Typische Anwendungsfälle:

- Suche nach Gemeinden über Name oder weitere Parameter
- Automatisierte Abfragen für Analysen oder Datenpipelines
- Nutzung in Jupyter Notebooks für explorative Datenanalysen

Die Installation erfolgt idealerweise in einer virtuellen Umgebung (z. B. mit uv).
Beispiel-Notebook: gebietsstammdaten_demo.ipynb.
