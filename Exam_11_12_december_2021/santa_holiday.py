days_stay = float(input())
type_room = input()
feedback = input()

price_stay = 0

if days_stay < 10:
    if type_room == "room for one person":
        price_stay = days_stay  * 18
    elif type_room == "apartment":
        price_stay = (days_stay - 1) * 25 * 0.7
    elif type_room == "president apartment":
        price_stay = (days_stay - 1) * 35 * 0.9

if 10 <= days_stay <= 15:
    if type_room == "room for one person":
        price_stay = (days_stay - 1) * 18
    elif type_room == "apartment":
        price_stay = (days_stay - 1) * 25 * 0.65
    elif type_room == "president apartment":
        price_stay = (days_stay - 1) * 35 * 0.85

if days_stay > 15:
    if type_room == "room for one person":
        price_stay = (days_stay - 1) * 18
    elif type_room == "apartment":
        price_stay = (days_stay - 1) * 25 * 0.5
    elif type_room == "president apartment":
        price_stay = (days_stay - 1) * 35 * 0.8


if feedback == "positive":
    price_stay += (price_stay * 0.25)
elif feedback == "negative":
    price_stay -= (price_stay * 0.1)

print(f"{price_stay:.2f}")

