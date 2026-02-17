## Gebietsstammdaten ZH: Variablenbeschrieb

### Grundprinzipien

#### Allgemein

Stammdaten sind oft als Wertetabellen mit **Code** und **Name** aufgebaut. Deshalb verwenden wir konsequent die Benennung:

- `<objekt>_code`
- `<objekt>_name`

Beispiel:

- `gemeinde_code`
- `gemeinde_name`

Der Code dient der eindeutigen Identifikation, der Name ist die offizielle bzw. fachlich gültige Bezeichnung.

---

#### Gebietstypen

Jedes Gebiet gehört zu einem Gebietstyp (z. B. Gemeinde, Bezirk, Kanton).  
Die Gebietstypen besitzen ebenfalls einen eigenen Code (`gebietstyp_code`).

Hinweise:

- Die Codes der Gebietstypen orientieren sich an der Systematik des Bundesamts für Statistik (BFS), insbesondere am Amtlichen Gemeindeverzeichnis (Attribut *Level*).
- Gebietstypen können – müssen aber nicht – in einer Hierarchie zueinander stehen (z. B. Kanton – Bezirk – Gemeinde). Dies wird aktuell über die Tabelle `gemeindezuweisungen` abgebildet.
- In der GIS-Welt werden andere Codes für Gebietstypen verwendet. Eine Mapping-Tabelle ist in Planung.

---

#### Eindeutigkeit

Ein Gebiet ist eindeutig bestimmt durch die Kombination von:

- `gebietstyp_code`
- `gebiet_code`

Damit können alle Gebiete grundsätzlich in einer gemeinsamen Tabelle geführt und flexibel ausgewertet werden. Eine entsprechende Erweiterung ist vorgesehen.

---

#### Unterschiedliche Variablennamen je Kontext

Ziel der **Gebietsstammdaten** ist es, die Variablennamen möglichst **allgemeingültig, standardisiert und kontextunabhängig verständlich** zu halten. Deshalb verzichten wir soweit möglich auf Abkürzungen.

Zu beachten ist jedoch, dass in anderen fachlichen oder technischen Kontexten teilweise andere Bezeichnungen etabliert sind.  
Der `gemeinde_code` heisst beispielsweise in anderen Systemen:

- `BFSNr`
- `MunicipalityID`
- `GDE_Nummer`


---
#### Tabelle Normdaten Gemeinden Kanton Zürich

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Typ</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>gebietstyp_code</td><td>Zahl</td><td>Code des Gebietstyps Gemeinde (BFS-Level)</td></tr>
    <tr><td>gemeinde_code</td><td>Zahl</td><td>Offizieller Code der Gemeinde (BFS-Nummer)</td></tr>
    <tr><td>gemeinde_name</td><td>Text</td><td>Offizieller Name der Gemeinde (BFS-Name)</td></tr>
  </tbody>
</table>


[zu den Daten](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich/distributions/6503)

---
#### Tabelle Normdaten Bezirke Kanton Zürich

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Typ</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>gebietstyp_code</td><td>Zahl</td><td>Code des Gebietstyps Bezirk (BFS-Level)</td></tr>
    <tr><td>bezirk_code</td><td>Zahl</td><td>Offizieller Code des Bezirks (BFS-Nummer)</td></tr>
    <tr><td>bezirk_name</td><td>Text</td><td>Offizieller Name des Bezirks (BFS-Name)</td></tr>
  </tbody>
</table>

[zu den Daten](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich/distributions/6505)

---
#### Tabelle Normdaten Raumplanungsregionen Kanton Zürich

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Typ</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>gebietstyp_code</td><td>Zahl</td><td>Code des Gebietstyps Raumplanungsregion (Verwendung im STAT)</td></tr>
    <tr><td>raumplanungsregion_code</td><td>Zahl</td><td>Offizieller Code der Raumplanungsregion (Vergabe durch ARE/Kantone)</td></tr>
    <tr><td>raumplanungsregion_name</td><td>Text</td><td>Offizieller Name der Raumplanungsregion (Vergabe durch ARE/Kantone)</td></tr>
  </tbody>
</table>

[zu den Daten](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich/distributions/6506)

---
#### Tabelle Gemeindezuweisungen (zu Bezirk und Raumplanungsregion) Kanton Zürich

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Typ</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>gemeinde_code</td><td>Zahl</td><td>Offizieller Code der Gemeinde (BFS-Nummer)</td></tr>
    <tr><td>gemeinde_name</td><td>Text</td><td>Offizieller Name der Gemeinde (BFS-Name)</td></tr>
    <tr><td>bezirk_code</td><td>Zahl</td><td>Offizieller Code des Bezirks (BFS-Nummer)</td></tr>
    <tr><td>bezirk_name</td><td>Text</td><td>Offizieller Name des Bezirks (BFS-Name)</td></tr>
    <tr><td>raumplanungsregion_code</td><td>Zahl</td><td>Code der Raumplanungsregion (Vergabe durch ARE/Kantone)</td></tr>
    <tr><td>raumplanungsregion_name</td><td>Text</td><td>Offizieller Name der Raumplanungsregion (Vergabe durch ARE/Kantone)</td></tr>
  </tbody>
</table>

[zu den Daten](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich/distributions/6563)

---
#### Tabelle Gemeindemutationen Kanton Zürich

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Typ</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>mutationstyp</td><td>Text</td><td>Mutationstyp (Namensänderung oder Fusion)</td></tr>
    <tr><td>gemeinde_code_alt</td><td>Zahl</td><td>Offizieller Code der Gemeinde (BFS-Nummer) vor der Mutation</td></tr>
    <tr><td>gemeinde_name_alt</td><td>Text</td><td>Offizieller Name der Gemeinde (BFS-Name) vor der Mutation</td></tr>
    <tr><td>gemeinde_code_neu</td><td>Zahl</td><td>Offizieller Code der Gemeinde (BFS-Nummer) nach der Mutation</td></tr>
    <tr><td>gemeinde_name_neu</td><td>Text</td><td>Offizieller Name der Gemeinde (BFS-Name) nach der Mutation</td></tr>
    <tr><td>mutationsdatum</td><td>Datum</td><td>Datum der Mutation</td></tr>
  </tbody>
</table>

[zu den Daten](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/datasets/3082@statistisches-amt-kanton-zuerich/distributions/6504)

---

