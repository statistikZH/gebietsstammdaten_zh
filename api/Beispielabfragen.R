
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
  req_body_json(list(gemeindename = "Bülach")) |>
  req_method("GET") |>
  req_perform() |>
  resp_body_json()

resp


#-------------------------------------------------------------------------------

# Bezirk und dazugehörende Gemeinden ausgeben

bezirk_code <- 101

resp <- req |>
  req_url_path_append("bezirke") |>
  req_url_path_append(bezirk_code) |>
  req_perform() |>
  resp_body_json()

resp

# Ausgabe des Bezirknamens
bezirk_name <- resp$bezirk$bezirk_name
bezirk_name

# Ausgabe Liste aller Gemeinden des Bezirks als Dataframe
gemeinden_df <- data.frame(
  gemeinde_code = sapply(resp$gemeinden, function(x) x$gemeinde_code),
  gemeinde_name = sapply(resp$gemeinden, function(x) x$gemeinde_name)
)
gemeinden_df
