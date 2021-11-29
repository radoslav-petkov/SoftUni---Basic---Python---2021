hall_rent_price = int(input())
cake_price = hall_rent_price * 0.20
drinks_price = cake_price * 0.55
animator_price = hall_rent_price / 3
total_cost = hall_rent_price + cake_price + drinks_price + animator_price
print(total_cost)