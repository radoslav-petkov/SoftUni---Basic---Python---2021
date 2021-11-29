powder_price_per_kg = float(input())
powder_kg = float(input())
sugar_kg = float(input())
eggs_cartons = int(input())
may_packages = int(input())

sugar_price_per_kg = powder_price_per_kg * 0.75
eggs_price_per_caton = powder_price_per_kg * 1.1
may_price_per_package = sugar_price_per_kg * 0.2

price_powder =  powder_price_per_kg * powder_kg
price_sugar =  sugar_price_per_kg * sugar_kg
eggs_price = eggs_price_per_caton * eggs_cartons
may_price = may_price_per_package * may_packages

total_sum = price_powder + price_sugar + eggs_price + may_price

print(f"{total_sum:.2f}")