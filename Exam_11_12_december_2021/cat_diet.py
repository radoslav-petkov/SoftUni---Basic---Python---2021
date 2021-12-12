percent_fat = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_count_calories = int(input())
percent_content_water = int(input())


total_grams_fat = ((percent_fat/100) * total_count_calories)/9
total_grams_proteins = ((percent_protein/100) * total_count_calories)/4
total_grams_carbs = ((percent_carbs/100)  * total_count_calories)/4
food_weight = total_grams_fat + total_grams_proteins + total_grams_carbs

calories_gram_food = total_count_calories/food_weight
calories = (100 - percent_content_water)/100 * calories_gram_food


print(f"{calories:.4f}")