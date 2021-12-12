destination = input()
reservation_days = input()
sleepovers_count = int(input())

cost = 0

if destination == "Germany":
    if reservation_days == "24-27":
        cost_per_night = 37
        cost = sleepovers_count * cost_per_night
    if reservation_days == "21-23":
        cost_per_night = 32
        cost = sleepovers_count * cost_per_night
    if reservation_days == "28-31":
        cost_per_night = 43
        cost = sleepovers_count * cost_per_night

if destination == "Italy":
    if reservation_days == "24-27":
        cost_per_night = 32
        cost = sleepovers_count * cost_per_night
    if reservation_days == "21-23":
        cost_per_night = 28
        cost = sleepovers_count * cost_per_night
    if reservation_days == "28-31":
        cost_per_night = 39
        cost = sleepovers_count * cost_per_night

if destination == "France":
    if reservation_days == "24-27":
        cost_per_night = 35
        cost = sleepovers_count * cost_per_night
    if reservation_days == "21-23":
        cost_per_night = 30
        cost = sleepovers_count * cost_per_night
    if reservation_days == "28-31":
        cost_per_night = 40
        cost = sleepovers_count * cost_per_night


print(f"Easter trip to {destination} : {cost:.2f} leva.")

















