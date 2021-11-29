strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2
total_price = strawberries_price * strawberries_quantity + raspberries_price * raspberries_quantity + \
              oranges_price * oranges_quantity + bananas_price * bananas_quantity
print(total_price)












