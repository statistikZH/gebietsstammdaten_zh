# Gebietsstammdaten ZH – Excel Add-In

Dieses Excel Add-In unterstützt die Arbeit mit Gemeindenamen, Gemeindecodes und Gebietszuweisungen für den Kanton Zürich. Es bietet Funktionen zur **Validierung** und **Anreicherung** von Gemeindedaten direkt in Excel. 
Die Funktionen verwenden die [API Gebietsstammdaten](https://gebietsstammdaten.statistik.zh.ch/) des Statistischen Amts des Kantons Zürich.

---

## Verwendung des Add-Ins

1. Datei `Gebietsstammdaten_V1.xlsm` auf dem Computer abspeichern und öffnen.
2. - Die zu bearbeitenden Daten in ein neues Worksheet in `Gebietsstammdaten_V1.xlsm` kopieren und da bearbeiten, oder:
   - `Gebietsstammdaten_V1.xlsm` und das zu bearbeitende Excel gleichzeitig offen haben. Hinweis: In diesem Fall kann es beim ersten Ausführen einer Funktion notwendig sein, die Schaltfläche **zweimal** zu klicken, bis sie ausgeführt wird.

Alle Makros befinden sich unter **Add-Ins** im Dropdown **„Gemeindestammdaten ZH“**. 

Es gibt drei Gruppen von Funktionen:

### 1 Daten validieren
[Daten validieren](Demo_validieren.mp4)
- **Gemeindename validieren (original Spalte behalten)**  
  Validiert die Gemeindenamen in einer neuen Spalte 
  - Grün: Name entspricht dem offiziellen BFS-Namen  
  - Orange: Mehrere Treffer – Dropdown zur Auswahl  
  - Rot: Kein Treffer  

- **Gemeindename in der selben Spalte nachvalidieren**  
  Führt die gleiche Validierung durch, überschreibt jedoch die Originalspalte (ist zur Nachvalidierung nach den vorgenommenen Korrekturen gedacht). Wenn alles grün ist, kann der gemeinde_code korrekt dem Gemeindenamen zugeordnet werden.

### 2 Daten anreichern

[Demo_Daten_anreichern_1.mp4](https://github.com/statistikZH/gebietsstammdaten_zh/issues/2#issue-3813182829)

- **gemeinde_code bzw. BFSNr. zu Gemeindename mappen**  
  Fügt rechts neben dem Code die offizielle Gemeinde ein.

[Daten anreichern](Demo_Daten_anreichern_2.mp4)

- **Gemeindename zu gemeinde_code mappen**  
  Ermittelt zum offiziellen Gemeindenamen des BFS den zughörigen Gemeinde-Code (BFSNr).

- **Gebietszuweisungen zu gemeinde_code mappen**  
  Ermittelt Bezirk, Raumplanungsregion und weitere Attribute anhand des Gemeinde-Codes.

- **Bezirk zu gemeinde_code mappen**  
  Fügt Bezirk-Code und Bezirk-Name rechts neben dem Gemeinde-Code ein.

- **Raumplanungsregion zu gemeinde_code mappen**  
  Fügt Raumplanungsregion-Code und Name rechts neben dem Gemeinde-Code ein.

### 3 Daten konvertieren
[Daten konvertieren](Demo_Daten_konvertieren.mp4)
- **Ausgewählte Zellen in Werte umwandeln**  
  Wandelt alle Formeln in der markierten Auswahl in feste Werte um. Das kann vor allem aus Performance-Gründen sehr nützlich sein.  

- **Einfärbungen und Dropdown-Listen aus ausgewählten Zellen entfernen**  
  Entfernt Formatierungen zur Datenvalidierungen (Dropdowns) aus der Auswahl.

---
## Excel-Formeln

[Formeln anwenden](Demo_Formeln_anwenden.mp4)

Die folgenden Funktionen können auch direkt in Excel-Zellen verwendet werden (als Formel, z. B. `=validate_gemeinde_name(A2)`):

| Formel | Beschreibung |
|--------|--------------|
| `=validate_gemeinde_name(gemeinde_name)` | Liefert die offiziellen Gemeindennamen als Text oder als Liste (mit `;` getrennt), basierend auf dem eingegebenen Gemeindename. |
| `=map_gemeinde_code_to_name(gemeinde_code)` | Liefert den Gemeindename zum angegebenen `gemeinde_code`. |
| `=map_gemeindezuweisungen_to_code(gemeinde_code; attribut)` | Liefert einen bestimmten Attributwert (z. B. `gemeinde_name`, `bezirk_code`) zu einem `gemeinde_code`. |

> Hinweis: Alle Formeln rufen die API auf. Stell sicher, dass eine Internetverbindung besteht.

## Tipps

- Für die Arbeit in größeren Tabellen empfiehlt es sich, zuerst die Validierung durchzuführen, anschließend die Anreicherung.
- Vor Änderungen empfiehlt es sich, die Originaldatei zu sichern.
- Die Funktionen arbeiten am zuverlässigsten, wenn die Gemeinde-Spalte **keine leeren Zeilen** enthält.

---

## Lizenz

Dieses Repository steht unter [MIT Lizenz](LICENSE). Sie dürfen die Makros frei verwenden, verändern und weitergeben.
