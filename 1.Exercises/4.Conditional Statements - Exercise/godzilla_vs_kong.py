budget = float(input())
number_of_extras = float(input())
price_for_clothes_for_one_extra = float(input())

price_for_decor = budget * 0.10
price_for_clothes = number_of_extras * price_for_clothes_for_one_extra

if number_of_extras > 150:
    price_for_clothes = price_for_clothes - (price_for_clothes * 0.10)

total_costs = price_for_decor + price_for_clothes

if total_costs > budget:
    needed_money = total_costs - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    left_money = budget - total_costs
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")


