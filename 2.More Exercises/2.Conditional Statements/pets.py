from math import floor, ceil

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

needed_food_dog = days * dog_food_per_day
needed_food_cat = days * cat_food_per_day
needed_food_turtle = days * (turtle_food_per_day / 1000)
total_food = needed_food_dog + needed_food_cat + needed_food_turtle

if total_food <= food_left:
    leftovers = floor(food_left - total_food)
    print(f"{leftovers} kilos of food left.")
else:
    needed_kg = ceil(total_food - food_left)
    print(f"{needed_kg} more kilos of food are needed.")