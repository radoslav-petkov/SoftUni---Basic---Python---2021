import math

price_per_racket = float (input())
count_rackets = int(input ())
count_trainers = int(input())


sum_rackets = count_rackets * price_per_racket
sum_trainers = count_trainers * (price_per_racket / 6)
sum_equipment = 0.20 * (sum_rackets + sum_trainers)

expenses = sum_rackets + sum_trainers + sum_equipment
sum_djokovic = expenses / 8
sum_sponsors = 7 / 8 * expenses

print(f'Price to be paid by Djokovic {math.floor(sum_djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(sum_sponsors)}')














