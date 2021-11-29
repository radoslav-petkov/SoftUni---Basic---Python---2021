from math import floor, ceil

x = int(input())
y = float(input())
z = int(input())
workers_count = int(input())

grape = x * y
wine = 0.4 * (grape / 2.5)
litres_left = abs(wine - z)
wine_for_one_workier = litres_left / workers_count

if wine >= z:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(litres_left)} liters left -> {ceil(wine_for_one_workier)} liters per person.")

else:
    print(f"It will be a tough winter! More {floor(litres_left)} liters wine needed.")













