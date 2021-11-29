rykav = float(input())
predna_4ast = float(input())
plat = input()
vratovryzka = input()

price = 0

razmer_riza = rykav * 2 + predna_4ast * 2
razmer_riza *= 1.1
razmer_riza /= 100

if plat == 'Linen':
    price = razmer_riza * 15
elif plat == 'Cotton':
    price = razmer_riza * 12
elif plat == 'Denim':
    price = razmer_riza * 20
elif plat == 'Twill':
    price = razmer_riza * 16
elif plat == 'Flannel':
    price = razmer_riza * 11

price += 10

if vratovryzka == 'Yes':
    price *= 1.2

print(f'The price of the shirt is: {price:.2f}lv.')