movie_type = input()
rows = int(input())
cols = int(input())
price = 0

if movie_type == "Premiere":
    price = 12
elif movie_type == "Normal":
    price = 7.50
elif movie_type == "Discount":
    price = 5

capacity = rows * cols
money_earned = capacity * price

print(f"{money_earned:.2f} leva")

