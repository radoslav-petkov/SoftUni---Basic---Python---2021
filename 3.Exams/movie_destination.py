budget = float(input())
destination = input()
season = input()
days_count = int(input())

cost = 0

if destination == "Sofia":
    if season == "Winter":
        cost_per_day = 17000
        cost = cost_per_day * days_count
        cost += cost * 0.25
    elif season == "Summer":
        cost_per_day = 12500
        cost = cost_per_day * days_count
        cost += cost * 0.25

if destination == "Dubai":
    if season == "Winter":
        cost_per_day = 45000
        cost = cost_per_day * days_count
        cost -= cost * 0.30
    elif season == "Summer":
        cost_per_day = 40000
        cost = cost_per_day * days_count
        cost -= cost * 0.30

if destination == "London":
    if season == "Winter":
        cost_per_day = 24000
        cost = cost_per_day * days_count
    elif season == "Summer":
        cost_per_day = 20250
        cost = cost_per_day * days_count

if budget > cost:
    money_left = budget - cost
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
else:
    needed_money = cost - budget
    print(f"The director needs {needed_money:.2f} leva more!")















# На конзолата да се отпечата един ред:
#  Ако бюджета е достатъчен:
# "The budget for the movie is enough! We have {остатък от бюджета} leva left!"
#  Ако бюджета НЕ е достатъчен:
# "The director needs {нужна сума} leva more!"
# Резултатът да се закръгли до втората цифра след десетичния знак.
#
#
#
#



