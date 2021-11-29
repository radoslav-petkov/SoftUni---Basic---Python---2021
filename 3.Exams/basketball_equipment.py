practice_taxes = 365
shoes = practice_taxes * 0.60
outfit = shoes * 0.80
ball = outfit / 4
accessories = ball / 5

practice_taxes = int(input())

training_price_yearly = practice_taxes

price_shoes = training_price_yearly - (training_price_yearly * (40 / 100))
price_outfit = price_shoes - (price_shoes * (20 / 100))
price_ball = 1 / 4 * price_outfit
price_accessories = 1 / 5 * price_ball

sum_total_price = training_price_yearly + price_shoes + price_outfit + price_ball + price_accessories
print(f"{sum_total_price:.2f}")