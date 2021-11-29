period = input()
plan = input ()
internet = input ()
months_count = int(input())

price = 0
discount = 0

if period == "one":
    if plan == "Small":
        price = 9.98
    elif plan == "Middle":
        price = 18.99
    elif plan == "Large":
        price = 25.98
    elif plan == "ExtraLarge":
        price = 35.99

elif period == "two":
   if plan == "Small":
       price = 8.58
   elif plan == "Middle":
       price = 17.09
   elif plan == "Large":
       price = 23.59
   elif plan == "ExtraLarge":
       price = 31.79
   discount = 0.0375

if internet == "yes":
    if price <= 10:
         price += 5.5
    elif price <= 30 and price > 10:
         price += 4.35
    else:
         price += 3.85

total_price = price * months_count
total_price -= total_price * discount
print(f"{total_price:.2f} lv.")




