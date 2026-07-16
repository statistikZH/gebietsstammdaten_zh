# Reconcile-Service in OpenRefine

Kennt ihr das? Eine Excel-Liste mit Gemeindenamen aus fünf verschiedenen Quellen – mal mit Bindestrich, mal ohne, mal ein Tippfehler und nun soll die Liste möglichst schnell und zuverlässig einheitlich gemäss der aktuellen, offiziellen Namensgebung validiert und mit dem amtlichen Gemeindecode (BFS-Nr.) und der Bezirkszugehörigkeit versehen werden?

Genau dafür gibt es neu einen **Reconciliation-Service für Gebietsstammdaten**, den man direkt in **OpenRefine** einbinden kann! OpenRefine ist ein OpenSource-Tool und Kantosnapplikation, das man im AFI-Serviceportal bestellen kann. 

## Was macht der Reconcile-Service?

Er gleicht eure Freitext-Einträge automatisch mit offiziellen Zürcher Gebietseinheiten ab. Im Moment sind verfügbar:
- **Gemeinden**
- **Bezirke**
- **Raumplanungsregionen**

Statt manuell durch Listen zu scrollen und Namen zu vergleichen, übernimmt OpenRefine den Abgleich – inklusive Vorschlägen bei mehrdeutigen oder unsauberen Schreibweisen, und mit einer Vorschau der jeweiligen Gebietseinheit direkt im Tool.

## Ein konkretes Anwendungsbeispiel

**Ausgangslage:** Ihr habt eine Liste mit über 100 Zürcher Gemeinden aus einem alten Fachsystem – Spaltenname z. B. „Gemeinde", Werte wie „Bülach", „Illnau-Effretikon", vereinzelt auch veraltete oder leicht falsch geschriebene Namen. Ihr wollt diese Liste mit einem aktuellen Datensatz (z. B. Steuerdaten, Schülerzahlen, GIS-Layer) über die Gemeindenummer verknüpfen.

**So geht's in OpenRefine:**

1. **Daten importieren:** CSV/Excel mit der Spalte „Gemeinde" in OpenRefine laden.
2. **Reconcile starten:** Auf die Spalte klicken → *Reconcile* → *Start reconciling…*
3. **Service hinzufügen:** *Add Standard Service…* und folgende URL eintragen: `https://gebietsstammdaten.statistik.zh.ch/api/reconcile`
4. **Typ wählen:** „Gemeinde" als Entitätstyp auswählen (alternativ „Bezirk" oder „Raumplanungsregion", je nach Bedarf).
5. **Abgleichen lassen:** OpenRefine schlägt für jede Zeile die passende amtliche Gemeinde vor – bei eindeutigen Treffern automatisch, bei Unsicherheiten mit Score und Vorschau zur manuellen Kontrolle.
6. **Anreichern:** Über *Add columns from reconciled values* lassen sich zusätzliche Attribute wie der Gemeindecode (Bfs-Nr.), den zughörigen Bezirk oder auch ein direkter Link in GIS-ZH.

**Resultat:** Aus einer unsauberen Namensliste wird in wenigen Minuten ein sauber referenzierter Datensatz mit Gebietscode – bereit für Verknüpfungen, Visualisierungen oder GIS-Anwendungen.

## Warum Gebietstammdaten in OpenRefine verwenden?

- **Zeitersparnis:** Kein manuelles Abgleichen und Nachschlagen von Gemeindenamen mehr.
- **Konsistenz:** Alle Ämter referenzieren dieselben, offiziellen und aktuellen Gebietsnamen und -codes.
- **Niederschwellig:** Keine Programmierkenntnisse nötig, funktioniert direkt in OpenRefine.