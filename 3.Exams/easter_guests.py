from math import ceil

guest_count = int(input())
budget = int(input())

cozunak_count = ceil(guest_count / 3)
eggs_count = guest_count * 2
total_sum = (4 * cozunak_count) + (0.45 * eggs_count)

if budget >= total_sum:
    money_left = budget - total_sum
    print(f"Lyubo bought {cozunak_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {money_left:.2f} lv. left.")
else:
    money_needed = total_sum - budget
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {money_needed:.2f} lv. more.")











