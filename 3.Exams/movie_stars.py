budget_left = float(input())
honorar_actor = 0
actor_name = input()

while actor_name != "ACTION":

    if len(actor_name) <= 15:
        honorar_actor = float(input())
    else:
        honorar_actor = budget_left * 20 / 100

    budget_left -= honorar_actor

    if budget_left <= 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        break

    actor_name = input()

if budget_left > 0:
    print(f"We are left with {budget_left:.2f} leva.")