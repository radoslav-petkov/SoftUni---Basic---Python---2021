budget = float(input())
number_of_graphics_card = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

graphics_card = 250

total_graphics_card = number_of_graphics_card * graphics_card
total_processors = (total_graphics_card * 0.35) * number_of_processors
total_ram = (total_graphics_card * 0.10) * number_of_ram

total_price = total_graphics_card + total_processors + total_ram

if number_of_graphics_card > number_of_processors:
    total_price = total_price - (total_price * 0.15)

budget_left = abs(total_price - budget)

if budget >= total_price:
    print(f"You have {budget_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {budget_left:.2f} leva more!")