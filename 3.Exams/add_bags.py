price_bag_over_20kg = float(input())
bags_weight = float(input())
days_to_journey = int(input())
bag_numbers = int(input())
bags_price = 0

if bags_weight < 10:
    bags_price = 0.2 * price_bag_over_20kg
elif 10 <= bags_weight <= 20:
    bags_price = 0.5 * price_bag_over_20kg
if bags_weight > 20:
    bags_price = price_bag_over_20kg

if days_to_journey > 30:
     bags_price = bags_price * 1.1

elif 7 <= days_to_journey <= 30:
    bags_price = bags_price * 1.15

elif days_to_journey < 7:
    bags_price = bags_price * 1.4

total_price = bags_price * bag_numbers

print(f"The total price of bags is: {total_price:.2f} lv.")