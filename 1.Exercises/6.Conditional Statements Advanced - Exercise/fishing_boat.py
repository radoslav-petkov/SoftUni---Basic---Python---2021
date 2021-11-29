budget = int(input())
season = input()
fisher_count = int(input())

rent_price = 4200
if season == "Spring":
    rent_price = 3000
elif season == "Winter":
    rent_price = 2600

if fisher_count <= 6:
    rent_price *= 0.9
elif fisher_count <= 11:
    rent_price *= 0.85
else:
    rent_price *= 0.75

if fisher_count % 2 == 0 and not season == "Autumn":
    rent_price *= 0.95

result = abs(rent_price - budget)

if budget >= rent_price:
    print(f"Yes! You have {result:.2f} leva left.")
else:
    print(f"Not enough money! You need {result:.2f} leva.")