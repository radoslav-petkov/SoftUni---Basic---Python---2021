profit = float (input())

collected_money = 0

name = input()
while name != 'Party!':
    cocktails_count = int (input())
    price = len(name) * cocktails_count

    if price % 2 != 0:
       price -= price * 0.25

    collected_money += price
    if collected_money >= profit:
        break

    name = input()

if name == 'Party!':
    print(f'We need {profit - collected_money:.2f} leva more.')
else:
    print('Target acquired.')
print(f'Club income - {collected_money:.2f} leva. ')