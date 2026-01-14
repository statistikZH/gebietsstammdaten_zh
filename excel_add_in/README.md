# Gebietsstammdaten ZH – Excel Add-In

Dieses Excel Add-In unterstützt die Arbeit mit Gemeindenamen, Gemeindecodes und Gebietszuweisungen für den Kanton Zürich. Es bietet Funktionen zur **Validierung** und **Anreicherung** von Gemeindedaten direkt in Excel. 
Die Funktionen verwenden die [API Gebietsstammdaten](https://gebietsstammdaten.statistik.zh.ch/) des Statistischen Amts des Kantons Zürich.

---

## Verwendung
1. Datei `Gebietsstammdaten_V1.xlsm` auf dem Computer abspeichern und öffnen.
2a. Die zu bearbeitenden Daten in ein neues Worksheet in `Gebietsstammdaten_V1.xlsm` kopieren und da bearbeiten, oder:
2b. `Gebietsstammdaten_V1.xlsm` und das zu bearbeitende Excel gleichzeitig offen haben.
> Hinweis: In diesem Fall kann es beim ersten Ausführen einer Funktion notwendig sein, die Schaltfläche **zweimal** zu klicken, bis sie ausgeführt wird.

Alle Makros befinden sich unter **Add-Ins** im Dropdown **„Gemeindestammdaten ZH“**. 
Dort gibt es drei Gruppen:

### 1 Daten validieren

- **Gemeindename validieren (original Spalte behalten)**  
  Validiert die Gemeindenamen in einer neuen Spalte 
  - Grün: Name entspricht dem offiziellen BFS-Namen  
  - Orange: Mehrere Treffer – Dropdown zur Auswahl  
  - Rot: Kein Treffer  

- **Gemeindename in der selben Spalte nachvalidieren**  
  Führt die gleiche Validierung durch, überschreibt jedoch die Originalspalte (ist zur Nachvalidierung nach den vorgenommenen Korrekturen gedacht). Wenn alles grün ist, kann der gemeinde_code korrekt dem Gemeindenamen zugeordnet werden.

### 2 Daten anreichern

- **gemeinde_code bzw. BFSNr. zu Gemeindename mappen**  
  Fügt rechts neben dem Code die offizielle Gemeinde ein.

- **Gemeindename zu gemeinde_code mappen**  
  Ermittelt zu einem Gemeindename den offiziellen Code.

- **Gebietszuweisungen zu gemeinde_code mappen**  
  Ermittelt Bezirk, Raumplanungsregion und weitere Attribute anhand des Codes.

- **Bezirk zu gemeinde_code mappen**  
  Fügt Bezirk-Code und Bezirk-Name rechts neben dem Gemeinde-Code ein.

- **Raumplanungsregion zu gemeinde_code mappen**  
  Fügt Raumplanungsregion-Code und Name rechts neben dem Gemeinde-Code ein.

### 3 Daten konvertieren

- **Ausgewählte Zellen in Werte umwandeln**  
  Wandelt alle Formeln in der markierten Auswahl in feste Werte um.  
  - Achtung: Leere Zellen oder Zellen ohne Formel werden ignoriert.

- **Einfärbungen und Dropdown-Listen aus ausgewählten Zellen entfernen**  
  Entfernt Formatierungen und Datenvalidierungen (Dropdowns) aus der Auswahl.

---

## Tipps

- Für die Arbeit in größeren Tabellen empfiehlt es sich, zuerst die Validierung durchzuführen, anschließend die Anreicherung.
- Vor Änderungen empfiehlt es sich, die Originaldatei zu sichern.
- Die Funktionen arbeiten am zuverlässigsten, wenn die Gemeinde-Spalte **keine leeren Zeilen** enthält.

---

## Lizenz

Dieses Repository steht unter [MIT Lizenz](LICENSE). Sie dürfen die Makros frei verwenden, verändern und weitergeben.
