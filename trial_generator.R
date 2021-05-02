

library(tidyverse)


## Les données en entrée

price_list = c(80:420 / 100)
#label_list = c("square", "circle", "triangle", "star", "cross")
label_list = c("carré", "cercle", "triangle", "étoile", "croix")
nutrition_list = c("A", "B", "C", "D", "E")

set.seed(42)

nb_products = 200

product_list = data.frame(
  price = sample(price_list, nb_products, replace = TRUE),
  label = sample(label_list, nb_products, replace = TRUE),
  nutrition = sample(nutrition_list, nb_products, replace = TRUE)
)

nb_rounds = 30
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

good_recommendation_found = FALSE
random_recommendation_found = FALSE
bad_recommendation_found = FALSE

while (! (good_recommendation_found & random_recommendation_found & bad_recommendation_found) ){

if (!good_recommendation_found){
  # On génère des valeurs pour les labels
  label_good_values = sample(label_values, 5)[1:5]
  names(label_good_values) = names(label_values)
  # On génère des valeurs pours la qualité nutritionnelle
  nutrition_good_values = sample(nutrition_values, 5)[1:5]
  names(nutrition_good_values) = names(nutrition_values)
  # On génère une valeur pour le prix
  good_price_factor = sample(-20:10/10,1)
}
if (!random_recommendation_found){
  # On génère des valeurs pour les labels
  label_random_values = sample(label_values, 5)[1:5]
  names(label_random_values) = names(label_values)
  # On génère des valeurs pours la qualité nutritionnelle
  nutrition_random_values = sample(nutrition_values, 5)[1:5]
  names(nutrition_random_values) = names(nutrition_values)
  # On génère une valeur pour le prix
  random_price_factor = sample(-20:10/10,1)
}
if (!bad_recommendation_found){
  # On génère des valeurs pour les labels
  label_bad_values = sample(label_values, 5)[1:5]
  names(label_bad_values) = names(label_values)
  # On génère des valeurs pours la qualité nutritionnelle
  nutrition_bad_values = sample(nutrition_values, 5)[1:5]
  names(nutrition_bad_values) = names(nutrition_values)
  # On génère une valeur pour le prix
  bad_price_factor = sample(-20:10/10, 1)
}



round_list = round_list%>%
  mutate(
    
    # perfect_rec
    label_points = as.numeric(label_values[label]),
    nutrition_points = as.numeric(nutrition_values[nutrition]),
    total_points = label_points + nutrition_points - price,
    
    # good_rec
    label_good_points = as.numeric(label_good_values[label]),
    nutrition_good_points = as.numeric(nutrition_good_values[nutrition]),
    total_good_points = label_good_points + nutrition_good_points + good_price_factor * price,
    
    # random_rec
    label_random_points = as.numeric(label_random_values[label]),
    nutrition_random_points = as.numeric(nutrition_random_values[nutrition]),
    total_random_points = label_random_points + nutrition_random_points + random_price_factor * price,
    
    # bad_rec
    label_bad_points = as.numeric(label_bad_values[label]),
    nutrition_bad_points = as.numeric(nutrition_bad_values[nutrition]),
    total_bad_points = label_bad_points + nutrition_bad_points + bad_price_factor * price

  )%>%
  group_by(round)%>%
  mutate(
    max_points = max(total_points),
    min_points = min(total_points),
    mean_points = mean(total_points),
    max_good_points = max(total_good_points),
    max_random_points = max(total_random_points),
    max_bad_points = max(total_bad_points)
  )%>%
  ungroup()%>%
  mutate(
    perfect_rec = (max_points == total_points),
    good_rec = (max_good_points == total_good_points),
    random_rec = (max_random_points == total_random_points),
    bad_rec = (max_bad_points == total_bad_points)
    )%>%
  select(
    round, order,
    label, nutrition, price, total_points, 
    perfect_rec, good_rec, random_rec, bad_rec
  )


scores = round_list%>%
  group_by(round)%>%
  summarise(
    max_points = max(total_points),
    min_points = min(total_points),
    mean_points = mean(total_points),
    good_score = sum(good_rec * total_points),
    random_score = sum(random_rec * total_points),
    bad_score = sum(bad_rec * total_points),
  )%>%
  ungroup()%>%
  summarise(
    total_max_points = sum(max_points),
    total_min_points = sum(min_points),
    total_mean_points = sum(mean_points),
    good_score = sum(good_score),
    random_score = sum(random_score),
    bad_score = sum(bad_score),
  )

if ( abs(scores$good_score - 0.8*scores$total_max_points) < 5){
  good_recommendation_found = TRUE
}


if ( abs(scores$random_score - scores$total_mean_points) < 5){
  random_recommendation_found = TRUE
}
  

if ( abs(scores$bad_score - 0.5 * scores$total_mean_points) < 5){
  bad_recommendation_found = TRUE
}


}



#write.csv(round_list, file = "D:/Users/Louise/Desktop/PSE/Thèse/LEEP_pilot/Github/Pilot_LEEP_RS/trial_set.csv")
write.csv(round_list, file = "D:/Users/Louise/Desktop/PSE/Thèse/LEEP_pilot/Github/Pilot_LEEP_RS/trial_set_FR.csv")
