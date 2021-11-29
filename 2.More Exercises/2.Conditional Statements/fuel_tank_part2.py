fuel_type = str(input())
fuel_quantity = float(input())
discount_card = str(input())
price= float()

if discount_card == "Yes" and fuel_type == "Gas":
    if fuel_quantity > 25:
        price = 0.9*(0.85 * fuel_quantity)
    elif 20 < fuel_quantity <= 25:
        price = 0.92*(0.85 * fuel_quantity)
    else:
        price = 0.85 * fuel_quantity
if discount_card == "No" and fuel_type == "Gas":
    if fuel_quantity > 25:
        price = 0.9 * (0.93*fuel_quantity)
    elif 20 < fuel_quantity <= 25:
        price = 0.92 * (0.93*fuel_quantity)
    else:
        price = 0.93*fuel_quantity
if discount_card == "Yes" and fuel_type == "Diesel":
    if fuel_quantity > 25:
        price = 0.9*(2.21 * fuel_quantity)
    elif 20 < fuel_quantity <= 25:
        price = 0.92*(2.21 * fuel_quantity)
    else:
        price = 2.21 * fuel_quantity
if discount_card == "No" and fuel_type == "Diesel":
    if fuel_quantity > 25:
        price = 0.9 * (2.33 * fuel_quantity)
    elif 20 < fuel_quantity <= 25:
        price = 0.92 * (2.33 * fuel_quantity)
    else:
        price = 2.33 * fuel_quantity
if discount_card == "Yes" and fuel_type == "Gasoline":
    if fuel_quantity > 25:
        price = 0.9*(2.04 * fuel_quantity)
    elif 20 < fuel_quantity <= 25:
        price = 0.92 * (2.04 * fuel_quantity)
    else:
        price = 2.04 * fuel_quantity
if discount_card == "No" and fuel_type == "Gasoline":
    if fuel_quantity > 25:
        price = 0.9 * (2.22 * fuel_quantity)
    elif 20 < fuel_quantity <= 25:
        price = 0.92 * (2.22 * fuel_quantity)
    else:
        price = 2.22 * fuel_quantity

print(f'{price:.2f} lv.')