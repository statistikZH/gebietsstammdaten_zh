## API Gebietsstammdaten Beispielabfragen

### 🩺 Health-Check  

**GET** `/api/health`  
→ Prüft den Status der API

 **curl**
```bash
curl https://gebietsstammdaten.statistik.zh.ch/api/health
```
**R**
```r
# Paket installieren
# install.packages("httr2")

# Paket laden
library("httr2")

# Definieren der Basis URL
req <- request("https://gebietsstammdaten.statistik.zh.ch/api")

# API Status prüfen
resp <- req |>
  req_url_path_append("health") |>
  req_perform() |>
  resp_body_json()

resp
```

---

### Gemeindenamen suchen  

**POST** `/api/gemeinden/gemeindename`  
→ Liefert Kandidaten für offizielle Gemeindenamen und -codes

**curl**
```bash
curl -X POST \
'https://gebietsstammdaten.statistik.zh.ch/api/gemeinden/gemeindename' \
-H 'accept: */*' \
--data-urlencode "name=Züri"

```

**R**
```r
# Paket installieren
# install.packages("httr2")

# Paket laden
library("httr2")

# Definieren der Basis URL
req <- request("https://gebietsstammdaten.statistik.zh.ch/api")

# Gemeinde suchen
resp <- req |>
  req_url_path_append("gemeinden/gemeindename") |>
  req_body_json(list(name = "Bülach")) |>
  req_method("POST") |>
  req_perform() |>
  resp_body_json()

resp

```

---

### Bezirk und zugehörige Gemeinden  

**GET** `/api/bezirke/{bezirk_code}`  
→ Gibt Informationen zu einem Bezirk und seinen Gemeinden zurück  

**Beispiel:** Bezirk Zürich (`bezirk_code = 101`)

**curl**
```bash
curl https://gebietsstammdaten.statistik.zh.ch/api/bezirke/101
```

**R**
```r
# Paket installieren
# install.packages("httr2")

# Paket laden
library("httr2")

# Definieren der Basis URL
req <- request("https://gebietsstammdaten.statistik.zh.ch/api")

bezirk_code <- 101

resp <- req |>
  req_url_path_append("bezirke") |>
  req_url_path_append(bezirk_code) |>
  req_perform() |>
  resp_body_json()

resp
```

---

➡️ [**Zur API-Dokumentation →**](https://gebietsstammdaten.statistik.zh.ch/api/__docs__/#/)

🧪 **Beta-Hinweis:**  
Diese API befindet sich in einer Beta-Version.  
Rückmeldungen und Verbesserungsvorschläge sind willkommen!

