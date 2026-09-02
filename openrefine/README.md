# Reconcile-Service in OpenRefine

Der neue **Reconciliation-Service für Gebietsstammdaten** kann man direkt in OpenRefine einbinden. OpenRefine ist ein **OpenSource-Tool und Kantonsapplikation**, das man im AFI-Serviceportal bestellen kann. 

## Zu OpenRefine

Kennst du das? Du versuchst, inkonsistente Daten in Excel mit komplexen Formeln oder mühsamem Suchen-und-Ersetzen zu bereinigen, verlierst aber schnell den Überblick über die Änderungen, die Datei stürzt immer wieder ab und du versuchst über Dateikopien keine Daten zu verlieren. 

👉 Hier kommt OpenRefine ins Spiel. Man kann **OpenRefine als eine Art *Excel auf Steroiden* für die Datenaufbereitung** betrachten. 

### Warum OpenRefine statt Excel?
**Reproduzierbarkeit:** Jeder Schritt, den du ausführst, wird in einer Historie gespeichert. Du kannst jederzeit sehen, was du verändert hast und Schritte rückgängig machen.

**Intelligente Bereinigung mit Clustering:** Dank mächtiger Algorithmen (Clustering) findet OpenRefine Schreibfehler oder Variationen (z. B. «Zürich», «Zuerich», «Zürich »), die du dann gezielt bereinigen kannst.

**Sicherheit:** OpenRefine läuft lokal, du kannst also auch sensible Daten damit bearbeiten. Du kannst deine Daten aus verschiedenen Quelldateien wie Excel, csv, XML importieren und wiederum nach der Bearbeitung in verschiedenen Formaten wieder exportieren. 

Du findest viele weitere Gründe für OpenRefine im [User Manual](https://openrefine.org/docs) Es gibt auch zahlreiche Online-Tutorials. Ein Beispiel wurde vom Landesarchiv Baden-Württemberg erarbeitet:

👉 [OpenRefine Workshops FDMLab](https://fdmlab.landesarchiv-bw.de/workshops/)

## Was macht der Gebietsstammdaten Reconcile-Service?

Er gleicht Freitext-Einträge automatisch mit offiziellen Zürcher Gebietsnamen ab. Im Moment sind verfügbar:

- **Gemeinden**
- **Bezirke**
- **Raumplanungsregionen**

## Ein konkretes Anwendungsbeispiel

**Ausgangslage:** Eine Liste mit über 100 Zürcher Gemeinden aus einem alten Fachsystem – Spaltenname z. B. „Gemeinde", Werte wie „Bülach", „Illnau-Effretikon", vereinzelt auch veraltete oder leicht falsch geschriebene Namen. Nun sollen die Gemeindenamen mit dem offiziellen Gemeindenamen des BFS abgeglichen und mit weiteren Daten (z. B. Steuerdaten, Schülerzahlen, GIS-Layer) über den Gemeindecode verknüpft werden.

**So geht's in OpenRefine:**

1. **Daten importieren:** CSV/Excel in OpenRefine laden.
2. **Reconcile starten:** Auf die Spalte mit den Gemeindenamen klicken → *Reconcile* → *Start reconciling…*
3. **Service hinzufügen:** *Add Standard Service…* und folgende URL eintragen: `https://gebietsstammdaten.statistik.zh.ch/api/reconcile`
4. **Typ wählen:** „Gemeinde" als Entitätstyp auswählen (alternativ „Bezirk" oder „Raumplanungsregion").
5. **Abgleichen lassen:** OpenRefine schlägt für jede Zeile die passende amtliche Gemeinde vor – bei eindeutigen Treffern automatisch, bei Unsicherheiten mit Score und Vorschau zur manuellen Kontrolle.
6. **Anreichern:** Über *Add columns from reconciled values* lassen sich zusätzliche Attribute wie der Gemeindecode (Bfs-Nr.), den zughörigen Bezirk oder auch ein direkter Link in GIS-ZH.
