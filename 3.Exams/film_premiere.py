projection_name = input()
packet = input()
tickets_cnt = int(input())

ticket_price = 0

if projection_name == 'John Wick':
   if packet == 'Drink':
       ticket_price = 12
   elif packet == 'Popcorn':
       ticket_price = 15
   elif packet == 'Menu':
       ticket_price = 19

elif projection_name == 'Star Wars':
    if packet == 'Drink':
        ticket_price = 18
    elif packet == 'Popcorn':
        ticket_price = 25
    elif packet == 'Menu':
        ticket_price = 30

elif projection_name == 'Jumanji':
    if packet == 'Drink':
        ticket_price = 9
    elif packet == 'Popcorn':
        ticket_price = 11
    elif packet == 'Menu':
        ticket_price = 14

total_price = tickets_cnt * ticket_price

discount_value = 0
if projection_name == 'Star Wars' and tickets_cnt >= 4:

     discount_value = 0.3 * total_price
elif projection_name == 'Jumanji' and tickets_cnt == 2:
     discount_value = 0.15 * total_price
total_price -= discount_value
print(f'Your bill is {total_price:.2f} leva.')
























