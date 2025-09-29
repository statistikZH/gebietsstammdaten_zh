## Script-Vorlagen

Hier stehen Script-Vorlagen zur Verfügung, um aus den **Gebietsstammdaten** im [Kantonalen Datenkatalog](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich) 
weitere Daten zu generieren.


### Historisierung der Gemeindecodes und -namen

Das Script [Gemeinden_ZH_HIST.R](Gemeinden_ZH_HIST.R) lädt Gebietsstammdaten zu Gemeindemutationen (Namensänderungen und Fusionen)
und den Normdaten der aktuellen Gemeinden. 

Damit wird für jedes Jahr rückwärts vom aktuellen Jahr bis 1990 eine Historisierung erstellt:
- Startpunkt: aktuelle Gemeindecodes und -namen mit dem aktuellem Jahr
- Für jedes frühere Jahr werden Mutationen berücksichtigt, d.h. wenn eine Mutation stattfand, wird rückwärts der alte Gemeindecode/Name übernommen.

Ergebnis:
- Eine vollständige Zeitreihe aller Gemeinden von heute bis 1990, gespeichert als [CSV-Datei](script_vorlagen/daten).
