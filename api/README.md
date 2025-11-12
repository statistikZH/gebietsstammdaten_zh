> ## 🧩 API Gebietsstammdaten Beispiel-Abfragen
>
> ### 🩺 Health-Check  
>
> **GET** `/api/health`  
> → Prüft den Status der API
>
> **curl**
> ```bash
> curl https://gebietsstammdaten.statistik.zh.ch/api/health
> ```
>
> **R**
> ```r
> library(jsonlite)
>
> data <- fromJSON("https://gebietsstammdaten.statistik.zh.ch/api/health")
> print(data)
> ```
>
> ---
>
> ### 🏘️ Gemeindenamen suchen  
>
> **POST** `/api/gemeinden/gemeinde_name`  
> → Liefert Kandidaten für offizielle Gemeindenamen und -codes
>
> **curl**
> ```bash
> curl -X POST https://gebietsstammdaten.statistik.zh.ch/api/gemeinden/gemeinde_name \
>      -H "Content-Type: application/json" \
>      -d '{"name": "Bülac"}'
> ```
>
> **R**
> ```r
> library(jsonlite)
> library(httr)
>
> url <- "https://gebietsstammdaten.statistik.zh.ch/api/gemeinden/gemeinde_name"
> body <- list(name = "Bülach")
>
> response <- POST(url, body = body, encode = "json")
> data <- content(response, as = "parsed", type = "application/json")
>
> print(data)
> ```
>
> ---
>
> ### 🗺️ Bezirk und zugehörige Gemeinden  
>
> **GET** `/api/bezirke/{bezirk_code}`  
> → Gibt Informationen zu einem Bezirk und seinen Gemeinden zurück  
>
> **Beispiel:** Bezirk Zürich (`bezirk_code = 101`)
>
> **curl**
> ```bash
> curl https://gebietsstammdaten.statistik.zh.ch/api/bezirke/101
> ```
>
> **R**
> ```r
> library(jsonlite)
>
> bezirk_code <- 101
> url <- paste0("https://gebietsstammdaten.statistik.zh.ch/api/bezirke/", bezirk_code)
>
> data <- fromJSON(url)
> print(data)
> ```
>
> ---
>
> ### 📦 Zur API-Dokumentation  
>
> ➡️ [**Zur API-Dokumentation →**](https://gebietsstammdaten.statistik.zh.ch/api/__docs__/#/)
>
> > 🧪 **Beta-Hinweis:**  
> > Diese API befindet sich in einer Beta-Version.  
> > Rückmeldungen und Verbesserungsvorschläge sind willkommen!

