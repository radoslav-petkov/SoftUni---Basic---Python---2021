minutes_per_walk = int(input ())
number_of_walks = int(input())
income_calories_per_day = int(input())
burned_calories = number_of_walks * minutes_per_walk * 5
if burned_calories >= income_calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")