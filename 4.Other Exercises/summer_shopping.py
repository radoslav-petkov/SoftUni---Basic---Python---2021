budget = int(input())
towel_price = float(input())
discount = int(input()) / 100

umbrella_price = 2/3 * towel_price
flip_flops_price =  0.75 * umbrella_price
bag_price = 1/3 * (flip_flops_price + towel_price)
total_price = towel_price + umbrella_price + flip_flops_price + bag_price
total_price = total_price (discount * total_price)

if budget >= total_price:
    money_left = budget - total_price
    print(f"Annie's sum is {total_price: .2f} lv. She has {money_left:.2f} lv. left.")
else:
    money_needed = total_price - budget
    print(f"Annie's sum is {total_price: .2f} lv. She needs {money_needed: .2f} lv. more.")