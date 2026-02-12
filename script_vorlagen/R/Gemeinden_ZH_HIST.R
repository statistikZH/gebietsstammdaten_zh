############################################################
# Titel: Historisierung der Zürcher Gemeindedaten
# Beschreibung:
# Dieses Skript lädt die offiziellen OGD-Daten des Kantons Zürich
# zu Gemeindemutationen (Namensänderungen, Fusionen)
# und den Normdaten der aktuellen Gemeinden. 
# Danach wird für jedes Jahr rückwärts vom aktuellen Jahr 
# bis 1990 eine Historisierung erstellt:
# - Startpunkt: aktuelle Gemeinden mit aktuellem Jahr
# - Für jedes frühere Jahr werden Mutationen berücksichtigt,
#   d.h. wenn eine Mutation (Fusion/Namensänderung) im Folgejahr
#   stattfand, wird rückwärts der alte Gemeindecode/Name übernommen.
# Ergebnis:
# Eine vollständige Zeitreihe aller Gemeinden von heute bis 1990,
# gespeichert als CSV-Datei.
#
# Autorin: Rebekka Plüss
# Datum: 29.09.2025
############################################################

library(readr)
library(dplyr)
library(lubridate)

#OGD Daten importieren und in Dataframe laden
gemeindemutationen_url <- "https://www.web.statistik.zh.ch/ogd/daten/ressourcen/KTZH_00003082_00006504.csv"
gemeinden_aktuell_url <- "https://www.web.statistik.zh.ch/ogd/daten/ressourcen/KTZH_00003082_00006503.csv"

gemeindmutationen <- read_csv(gemeindemutationen_url)
gemeinden_aktuell <- read_csv(gemeinden_aktuell_url)

# Aktuelles Jahr ermitteln
sysjahr <- as.integer(format(Sys.Date(), "%Y"))

# Sequenz von aktuellem Jahr bis 1990
jahre <- sysjahr:1990  

# Starte mit aktuellen Jahr als Basisjahr und 
# füge in die neue Tabelle "result" alle Daten aus "gemeinden_aktuell" 
# mit der zusätzlichen Spalte "Jahr" mit dem Wert des aktuellen Jahres hinzu.

result <- gemeinden_aktuell %>%
  mutate(jahr = sysjahr)

vorjahr <- sysjahr - 1

# Iteriere rückwärts ab dem Vorjahr
for (j in vorjahr:1990) {
  
  # Nimm die "letzte bekannte" Version aus dem Resultat vom Vorjahr
  tmp <- result %>% filter(jahr == j + 1)
  
  # Schaue nach, welche Mutationen im Jahr j+1 passiert sind
  mut_jahr <- gemeindmutationen %>%
    filter(year(mutationsdatum) == (j + 1))
  
  #Wenn es im Jahr j+1 Mutationen gegeben hat...
  if (nrow(mut_jahr) > 0) {
    # ...dann: Join mit Mutationstabelle: Wenn ein gemeinde_code oder gemeinde_name mutiert ist,
    # dann ersetze ihn durch den "alten" gemeinde_code und gemeinde_name
    tmp <- tmp %>%
      left_join(mut_jahr %>% 
                  select(gemeinde_code_neu, 
                         gemeinde_code_alt, 
                         gemeinde_name_alt),
                by = c("gemeinde_code" = "gemeinde_code_neu")) %>%
      mutate(
        gemeinde_code = ifelse(!is.na(gemeinde_code_alt), gemeinde_code_alt, gemeinde_code),
        gemeinde_name = ifelse(!is.na(gemeinde_name_alt), gemeinde_name_alt, gemeinde_name)
      ) %>%
      select(-gemeinde_code_alt, -gemeinde_name_alt)
  }
  
  tmp <- tmp %>% mutate(jahr = j)
  
  # Füge die Tabelle tmp zur Tabelle result hinzu
  result <- bind_rows(result, tmp)
}

# Ergebnis sortieren 
gemeinde_code_jahr <- result %>% arrange(desc(jahr), gemeinde_code)

# Als CSV speichern
write_csv(gemeinde_code_jahr, "daten/gemeinde_code_jahr.csv")
