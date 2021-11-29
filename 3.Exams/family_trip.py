budget = float(input())
sleepovers_count = int(input())
sleepover_price_per_night = float(input())
extra_expenses_percent = int(input())


if sleepovers_count > 7:
    sleepover_price_per_night -= sleepover_price_per_night * 0.05

total_sum = budget * (extra_expenses_percent / 100) + (sleepover_price_per_night * sleepovers_count)

if budget >= total_sum:
    money_left = budget - total_sum
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = total_sum - budget
    print(f"{money_needed:.2f} leva needed.")
