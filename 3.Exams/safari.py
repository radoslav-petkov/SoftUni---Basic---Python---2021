budget = float (input ())
fuel_liters_count = float(input())
day_of_the_week = input ()

fuel_price = fuel_liters_count * 2.10
guide_price = 100
total_price = fuel_price + guide_price

if day_of_the_week == 'Saturday':
    discount_percentage = 0.1
else:
    discount_percentage = 0.2

discount_value = discount_percentage * total_price
total_price -= discount_value

if budget >= total_price:
    money_left = budget - total_price
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    money_needed = total_price - budget
    print(f'Not enough money! Money needed: {money_needed:.2f} lv.')







