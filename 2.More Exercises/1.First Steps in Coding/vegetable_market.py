vegetables_price_per_kg = float(input())
fruit_price_per_kg = float(input())
total_vegetables_kg = int(input())
total_fruits_kg = int(input())

vegetables_total_sum = vegetables_price_per_kg * total_vegetables_kg
fruit_total_sum = fruit_price_per_kg * total_fruits_kg

total_sum = (vegetables_total_sum + fruit_total_sum) / 1.94

print(f"{total_sum:.2f}")






