budget = float(input())
season = input()
price = 0
location = 0
place_of_stay = 0
#
if budget <= 1000:
    place_of_stay = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

if 1000 < budget <= 3000:
    place_of_stay = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60

if budget > 3000:
    place_of_stay = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {place_of_stay} - {price:.2f}")

