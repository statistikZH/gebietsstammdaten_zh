## Gebietsstammdaten ZH: Variablenbeschrieb

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
    <tr><td>gebietstyp_code</td><td>Zahl</td><td>Code des Gebietstyps Gemeinde</td></tr>
    <tr><td>gemeinde_code</td><td>Zahl</td><td>Offizieller Code der Gemeinde (BFS-Nummer)</td></tr>
    <tr><td>gemeinde_name</td><td>Text</td><td>Offizieller Name der Gemeinde</td></tr>
  </tbody>
</table>


[zu den Daten]()

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
    <tr><td>gebietstyp_code</td><td>Zahl</td><td>Code des Gebietstyps Bezirk</td></tr>
    <tr><td>bezirk_code</td><td>Zahl</td><td>Offizieller Code des Bezirks (BFS-Nummer)</td></tr>
    <tr><td>bezirk_name</td><td>Text</td><td>Offizieller Name des Bezirks</td></tr>
  </tbody>
</table>

[zu den Daten]()

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
    <tr><td>gebietstyp_code</td><td>Zahl</td><td>Code des Gebietstyps Raumplanungsregion</td></tr>
    <tr><td>raumplanungsregion_code</td><td>Zahl</td><td>Offizieller Code der Raumplanungsregion</td></tr>
    <tr><td>raumplanungsregion_name</td><td>Text</td><td>Offizieller Name der Raumplanungsregion</td></tr>
  </tbody>
</table>

[zu den Daten]()

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
    <tr><td>gemeinde_name</td><td>Text</td><td>Offizieller Name der Gemeinde</td></tr>
    <tr><td>bezirk_code</td><td>Zahl</td><td>Offizieller Code des Bezirks (BFS-Nummer)</td></tr>
    <tr><td>bezirk_name</td><td>Text</td><td>Offizieller Name des Bezirks</td></tr>
    <tr><td>raumplanungsregion_code</td><td>Zahl</td><td>Code der Raumplanungsregion</td></tr>
    <tr><td>raumplanungsregion_name</td><td>Text</td><td>Offizieller Name der Raumplanungsregion</td></tr>
  </tbody>
</table>

[zu den Daten]()

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
    <tr><td>gemeinde_name_alt</td><td>Text</td><td>Offizieller Name der Gemeinde vor der Mutation</td></tr>
    <tr><td>gemeinde_code_neu</td><td>Zahl</td><td>Offizieller Code der Gemeinde (BFS-Nummer) nach der Mutation</td></tr>
    <tr><td>gemeinde_name_neu</td><td>Text</td><td>Offizieller Name der Gemeinde nach der Mutation</td></tr>
    <tr><td>mutationsdatum</td><td>Datum</td><td>Datum der Mutation</td></tr>
  </tbody>
</table>

[zu den Daten]()

---

