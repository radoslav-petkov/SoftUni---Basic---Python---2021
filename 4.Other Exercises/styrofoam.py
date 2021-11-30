import math

budget = float(input())
area_house = float(input())
windows = int(input())
styrofoam = float(input())
styrofoam_price = float(input())

area_house = area_house - 2.4 * area_house
area_house = area_house + area_house * 0.10
packets = math.ceil(area_house / styrofoam)
price = packets * styrofoam_price

diff = abs (budget - price)
if budget > price:
    print (f"Spent: {price:.2f}")
    print (f"Left:I {diff:.2f}")
else:
    print (f"Need more: {diff:.2f}")









