count = int(input())
type = input()
delivery = input()

price = 0
if type == '90X130':
    price = 110
    if count > 30 and count <= 60:
        price -= price * 0.05
    elif count > 60:
        price -= price * 0.08

elif type == '100X150':
    price = 140
    if count > 40 and count <= 80:
        price -= price * 0.06
    elif count > 80:
        price -= price * 0.1

elif type == '130X180':
    price = 190
    if count > 20 and count <= 50:
        price -= price * 0.07
    elif count > 50:
        price -= price * 0.12

elif type == '200X300':
    price = 250
    if count > 25 and count <= 50:
        price -= price * 0.09
    elif count > 50:
        price -= price * 0.14

total = count * price
if delivery == 'With delivery':
    total += 60

if count > 99:
    total -= total * 0.04

if count < 10:
    print('Invalid order')
else:
    print(f'{total:.2f} BGN')