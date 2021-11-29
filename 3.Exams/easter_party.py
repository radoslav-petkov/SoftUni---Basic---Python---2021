guest_count = int(input())
cover_per_person = float(input())
budget = float(input())


if 10 <= guest_count <= 15:
    cover_per_person -= cover_per_person * 0.15
elif 16 <= guest_count <= 20:
    cover_per_person -= cover_per_person * 0.20
elif guest_count >= 21:
    cover_per_person -= cover_per_person * 0.25

price_cake = 0.1 * budget
total_sum = guest_count * cover_per_person + price_cake

if budget > total_sum:
    money_left = budget - total_sum
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_needed = total_sum - budget
    print(f"No party! {money_needed:.2f} leva needed.")
















