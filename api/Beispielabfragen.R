
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

#-------------------------------------------------------------------------------

# Gemeinde suchen
resp <- req |>
  req_url_path_append("gemeinden/gemeindename") |>
  req_body_json(list(name = "Bülach")) |>
  req_method("POST") |>
  req_perform() |>
  resp_body_json()

resp

#-------------------------------------------------------------------------------

# Bezirk inkl. Gemeinde aufrufen
bezirk_code <- 101

resp <- req |>
  req_url_path_append("bezirke") |>
  req_url_path_append(bezirk_code) |>
  req_perform() |>
  resp_body_json()

resp