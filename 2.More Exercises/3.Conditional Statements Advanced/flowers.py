chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

all_flowers = chrysanthemums + roses + tulips
bouquet = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price

if holiday == 'Y':
    bouquet *= 1.15

if tulips > 10 and season == 'Spring':
    bouquet *= 0.95
elif roses >= 10 and season == 'Winter':
    bouquet *= 0.9

if all_flowers > 20:
    bouquet *= 0.80

final_price = bouquet + 2
print(f'{final_price:.2f}')
