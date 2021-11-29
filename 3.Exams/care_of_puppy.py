quantity_of_food_in_kg = int(input())
quantity_of_food_in_gr = quantity_of_food_in_kg * 1000


while True:
    current_food_in_gr = input()

    if current_food_in_gr == "Adopted":
        break

    quantity_of_food_in_gr -= int(current_food_in_gr)


if quantity_of_food_in_gr >= 0:
    print(f"Food is enough! Leftovers: {quantity_of_food_in_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(quantity_of_food_in_gr)} grams more.")




















