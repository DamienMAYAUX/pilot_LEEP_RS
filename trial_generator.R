

library(tidyverse)


## Les données en entrée

price_list = c(80:420 / 100)
label_list = c("square", "circle", "triangle", "star", "cross")
nutrition_list = c("A", "B", "C", "D", "E")

set.seed(42)

nb_products = 40

product_list = data.frame(
  price = sample(price_list, nb_products, replace = TRUE),
  label = sample(label_list, nb_products, replace = TRUE),
  nutrition = sample(nutrition_list, nb_products, replace = TRUE)
)

nb_rounds = 35
nb_products_per_round = 6

round_list = 
  bind_rows(
    map(1:nb_rounds, 
        function(i){
          product_list%>%
            .[sample(1:nb_products, nb_products_per_round),]%>%
            mutate(
              order = sample(1:nb_products_per_round, nb_products_per_round),
              round = i
            )
        })
  )


label_values = list()
for (shape in label_list){
  #label_values[[shape]] = sample(1:5, 1)
  # Le membre de droite est un hack pour chercher 
  # le rang de la première occurence dans le vecteur
  # et changer l'ordre
  label_values[[shape]] = 6 - sum(1:length(label_list) * (label_list == shape))
  
}

nutrition_values = list()
for (letter in nutrition_list){
  # Il serait sans doute plus pertinent d'utiliser des variables ordonnées
  nutrition_values[[letter]] = 6- sum(1:length(label_list) * (nutrition_list == letter))
  #nutrition_values[[letter]] = sample(1:5, 1)
}


### GENERER LES PREFERENCES QUI PRODUISENT LES RECOMMENDATIONS

round_list = round_list%>%
  mutate(
    label_points = as.numeric(label_values[label]),
    nutrition_points = as.numeric(nutrition_values[nutrition]),
    total_points = label_points + nutrition_points - price
  )%>%
  group_by(round)%>%
  mutate(
    max_points = max(total_points),
    min_points = min(total_points),
    mean_points = mean(total_points)
  )%>%
  ungroup()%>%
  mutate(perfect_rec = (max_points == total_points))%>%
  mutate(recA = FALSE, recB = TRUE, recC = FALSE, recD = FALSE)


scores = round_list%>%
  group_by(round)%>%
  summarise(
    max_points = max(total_points),
    min_points = min(total_points),
    mean_points = mean(total_points)
  )%>%
  ungroup()%>%
  summarise(
    total_max_points = sum(max_points),
    total_min_points = sum(min_points),
    total_mean_points = sum(mean_points)
  )

write.csv(round_list, file = "C:/Users/d.mayaux/Desktop/PSE/Thèse/LEEP_pilot/trial_set.csv")
