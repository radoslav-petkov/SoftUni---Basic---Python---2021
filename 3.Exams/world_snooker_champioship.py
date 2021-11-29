competition_stage = input()
type_ticket = input()
number_tickets = int(input())
photo = input()

total_price = 0
photo_sum = 0
discount_photo = False

if competition_stage == 'Quarter final' and type_ticket == 'Standard':
    total_price = number_tickets * 55.50
elif competition_stage == 'Quarter final' and type_ticket == 'Premium':
    total_price = number_tickets * 105.20
elif competition_stage == 'Quarter final' and type_ticket == 'VIP':
    total_price = number_tickets * 118.90

if competition_stage == 'Semi final' and type_ticket == 'Standard':
    total_price = number_tickets * 75.88
elif competition_stage == 'Semi final' and type_ticket == 'Premium':
    total_price = number_tickets * 125.22
elif competition_stage == 'Semi final' and type_ticket == 'VIP':
    total_price = number_tickets * 300.40

if competition_stage == 'Final' and type_ticket == 'Standard':
    total_price = number_tickets * 110.10
elif competition_stage == 'Final' and type_ticket == 'Premium':
    total_price = number_tickets * 160.66
elif competition_stage == 'Final' and type_ticket == 'VIP':
    total_price = number_tickets * 400


if 2500 < total_price <= 4000:
    total_price = total_price - (total_price * 0.10)
elif total_price > 4000:
    total_price = total_price - (total_price * 0.25)
    discount_photo = True

if photo == 'Y':
    photo_sum = number_tickets * 40
    total_price += photo_sum
    if discount_photo:
        total_price -= photo_sum
else:
    total_price = total_price

print(f'{total_price:.2f}')