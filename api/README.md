## Beispiel-Requests

### Health Check

**GET** `/api/health`  
→ API-Status prüfen

curl:
```bash
curl https://gebietsstammdaten.statistik.zh.ch/api/health
```
R:
```bash
library(jsonlite)

data <- fromJSON("gebietsstammdaten.statistik.zh.ch/api/health")
print(data)
```

### Gemeindenamen

**POST** `/api/gemeinden/suche`  
→ Kandidaten für offizielle Gemeindenamen und -codes

curl:
```bash
curl -X POST https://gebietsstammdaten.statistik.zh.ch/api/gemeinden/gemeinde_name -H "Content-Type: application/json" -d '{"name": "Bülac"}'
```

R: 
```bash
library(jsonlite)
library(httr)

url <- "https://gebietsstammdaten.statistik.zh.ch/api/gemeinden/gemeinde_name"
body <- list(name = "Bülach")

response <- POST(url, body = body, encode = "json")
data <- content(response, as = "parsed", type = "application/json")

print(data)
```

**GET**  `/api/bezirke/{bezirk_code}`
→ Bezirk und zugehörige Gemeinden

curl:
```bash
curl https://gebietsstammdaten.statistik.zh.ch/api/bezirke/102
```
