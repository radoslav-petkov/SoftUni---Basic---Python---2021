import math

peoples = int(input())
entry_fee = float(input ())
sunbed_price = float (input())
umbrella_price = float(input())

expenses = peoples * entry_fee + math.ceil(peoples/2) * umbrella_price + math.ceil(peoples * 0.75) * sunbed_price
print(f"{expenses:.2f} lv.")