

library(tidyverse)

## Principaux parametres

set.seed(42)

nb_products = 500

nb_rounds = 30
nb_products_per_round = 6

language = "FR"
#language = "EN"
s

price_list = c(80:580 / 100)
#price_prob = c(80:420 / 100)^-4 / sum( c(80:420 / 100)^-2  ) 

if (language == "FR"){
  label_list = c("carré", "cercle", "triangle", "étoile", "croix")
} else {
  label_list = c("square", "circle", "triangle", "star", "cross")
}

#label_prob = c(0.1, 0.1, 0.3, 0.3, 0.2)

nutrition_list = c("A", "B", "C", "D", "E")
#nutrition_prob = c(0.1, 0.2, 0.3, 0.3, 0.1)


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



## On genere la liste des produits

product_list = data.frame(
  price = sample(price_list, nb_products, replace = TRUE),
  label = sample(label_list, nb_products, replace = TRUE),
  nutrition = sample(nutrition_list, nb_products, replace = TRUE)
)




## On genere la liste des porduits de chaque round
## en piochant aleatoirement dans la liste des produits

good_round_list = FALSE

while (!good_round_list){
  
  # Je genere une liste de produits pour chaque round
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
  
  # Je teste l'absence de trend
  df_score = round_list%>%
    mutate(
      label_points = as.numeric(label_values[label]),
      nutrition_points = as.numeric(nutrition_values[nutrition]),
      total_points = label_points + nutrition_points - price,
    )%>%
    group_by(round)%>%
    summarise(
      max_points = max(total_points),
      min_points = min(total_points),
      mean_points = mean(total_points),
      second_max_points = max(total_points - 10 * (total_points == max_points)),
      second_min_points = min(total_points + 10 * (total_points == min_points))
    )%>%
    mutate(
      corr_max = cov(max_points, round),
      corr_min = cov(min_points, round),
      corr_mean = cov(mean_points, round),
      corr_second_max = cov(second_max_points, round),
      corr_second_min = cov(second_min_points, round),
    )
    
  if (df_score[1,7:11]%>% as.list()%>% map_dbl(~abs(.)<0.8)%>% sum() == 5 ){
    good_round_list = TRUE
  }
  
}


# On verifie visuellement que le résultat est convaincant
ggplot(df_score, aes(x = round))+
  geom_point(aes(y = max_points), color = "red")+
  geom_smooth(aes(y = max_points), color = "red", se = FALSE, method = "lm")+
  geom_point(aes(y = min_points), color = "green")+
  geom_smooth(aes(y = min_points), color = "green", se = FALSE, method = "lm")+
  geom_point(aes(y = mean_points), color = "blue")+
  geom_smooth(aes(y = mean_points), color = "blue", se = FALSE, method = "lm")+
  geom_point(aes(y = second_max_points), color = "purple")+
  geom_smooth(aes(y = second_max_points), color = "purple", se = FALSE, method = "lm")+
  geom_point(aes(y = second_min_points), color = "orange")+
  geom_smooth(aes(y = second_min_points), color = "orange", se = FALSE, method = "lm")
  





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


df_score = round_list%>%
  arrange(round, -total_points)%>%
  group_by(round)%>%
  mutate(
    rank = 1:n()
  )%>%
  summarise(
    max_points = max(total_points),
    min_points = min(total_points),
    mean_points = mean(total_points),
    good_score = sum(good_rec * total_points),
    random_score = sum(random_rec * total_points),
    bad_score = sum(bad_rec * total_points),
    good_rank = sum(good_rec * rank),
    random_rank = sum(random_rec * rank),
    bad_rank = sum(bad_rec * rank),
  )%>%
  ungroup()%>%
  mutate(
    total_max_points = sum(max_points),
    total_min_points = sum(min_points),
    total_mean_points = sum(mean_points),
    total_good_score = sum(good_score),
    total_random_score = sum(random_score),
    total_bad_score = sum(bad_score),
    corr_good = cov(good_score, round),
    corr_random = cov(random_score, round),
    corr_bad = cov(bad_score, round),
    corr_good_rank = cov(good_rank, round),
    corr_random_rank = cov(random_rank, round),
    corr_bad_rank = cov(bad_rank, round),
    corr_good_rank_good = cov(as.numeric(good_rank %in% c(1,2)), round),
    corr_bad_rank_bad = cov(as.numeric(bad_rank %in% c(5,6)), round),
    corr_random_rank_good = cov(as.numeric(random_rank %in% c(1,2)), round),
    nb_perfect_good = sum(max_points == good_score),
    nb_perfect_random = sum(max_points == random_score),
    nb_worst_random = sum(min_points == random_score),
    nb_worst_bad = sum(min_points == bad_score),
  )

if ( abs(df_score[1,"corr_good"])<0.5 &
     abs(df_score[1,"corr_good_rank_good"])<0.3 &
     abs(df_score[1,"corr_good_rank"])<0.5 &
     abs(df_score[1,"total_good_score"] - 0.5*(df_score[1,"total_mean_points"]+df_score[1,"total_max_points"])  ) < 5){
  good_recommendation_found = TRUE
}


if ( abs(df_score[1,"corr_random"])<0.5 &
     abs(df_score[1,"corr_random_rank_good"])<0.3 &
     abs(df_score[1,"corr_random_rank"])<0.5 &
     abs(df_score[1,"total_random_score"] - df_score[1,"total_mean_points"] ) < 5){
  random_recommendation_found = TRUE
}
  

if ( abs(df_score[1,"corr_bad"])<0.5 &
     abs(df_score[1,"corr_bad_rank_bad"])<0.3 &
     abs(df_score[1,"corr_bad_rank"])<0.5 &
     abs(df_score[1,"total_bad_score"] - 0.75 * (df_score[1,"total_min_points"]+df_score[1,"total_mean_points"]) ) < 5){
  bad_recommendation_found = TRUE
}


}

## On controle visuellement le resultat

# Le score obtenu
ggplot(df_score, aes(x = round))+
  geom_smooth(aes(y = max_points), color = "blue", se = FALSE, method = "lm")+
  geom_smooth(aes(y = min_points), color = "purple", se = FALSE, method = "lm")+
  geom_smooth(aes(y = mean_points), color = "black", se = FALSE, method = "lm")+
  geom_point(aes(y = good_score), color = "red")+
  geom_smooth(aes(y = good_score), color = "red", se = FALSE, method = "lm")+
  geom_point(aes(y = random_score), color = "orange")+
  geom_smooth(aes(y = random_score), color = "orange", se = FALSE, method = "lm")+
  geom_point(aes(y = bad_score), color = "yellow")+
  geom_smooth(aes(y = bad_score), color = "yellow", se = FALSE, method = "lm")

# Le rang du produit recommandé
ggplot(df_score, aes(x = round))+
  geom_smooth(aes(y = good_rank), color = "blue", se = FALSE, method = "lm")+
  geom_smooth(aes(y = random_rank), color = "purple", se = FALSE, method = "lm")+
  geom_smooth(aes(y = bad_rank), color = "black", se = FALSE, method = "lm")

# La probabilité que ce soit le meilleur ou le plus mauvais
ggplot(df_score, aes(x = round))+
  geom_smooth(aes(y = as.numeric(random_rank %in% c(1,2))), color = "black", se = FALSE, method = "lm")+
  geom_jitter(aes(y = as.numeric(random_rank %in% c(1,2))), color = "black", width = 0, height = 0.01)+
  geom_smooth(aes(y = as.numeric(bad_rank %in% c(5,6))), color = "purple", se = FALSE, method = "lm")+
  geom_jitter(aes(y = as.numeric(bad_rank %in% c(5,6))), color = "purple", width = 0, height = 0.01)+
  geom_smooth(aes(y = as.numeric(good_rank %in% c(1,2))), color = "blue", se = FALSE, method = "lm")+
  geom_jitter(aes(y = as.numeric(good_rank %in% c(1,2))), color = "blue", width = 0, height = 0.01)

df_score%>%
  mutate(
    se_max = var(max_points),
    se_good = var(good_score),
    se_random = var(random_score),
    se_bad = var(bad_score),
    se_min = var(min_points)
    )%>%
  select(se_max, se_good, se_random, se_bad, se_min)%>%
  unique()

## Gain max, moyen et min
df_score%>%
  select_at(grep("total.*((score)|(points))", names(df_score), value=TRUE))%>%
  unique()


## On sauvergarde
if (language == "FR"){
  write.csv(round_list, file = "D:/Users/Louise/Desktop/PSE/Thèse/LEEP_pilot/Github/Pilot_LEEP_RS/trial_set_FR.csv")
} else {
  write.csv(round_list, file = "D:/Users/Louise/Desktop/PSE/Thèse/LEEP_pilot/Github/Pilot_LEEP_RS/trial_set.csv")
}



