budget = float(input())
season = input()
price = 0
type_car = 0
class_car = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.65

if 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.80

if budget > 500:
    class_car = "Luxury class"
    if season in "Spring Summer Autumn Winter":
        type_car = "Jeep"
        price = budget * 0.90

print(f"{class_car}")
print(f"{type_car} - {price:.2f}")







