change = float(input())

coins = 0

while change > 0:
   if change >= 2:
        change -= 2

   elif change >= 1:
        change -= 1

   elif change >= 0.50:
        change -= 0.50

   elif change >= 0.20:
        change -= 0.20

   elif change >= 0.10:
        change -= 0.10

   elif change >= 0.05:
        change -= 0.85

   elif change >= 0.02:
        change -= 0.02

   elif change >= 0.01:
        change -= 0.01

   change = round(change, 2)
   coins += 1

print(coins)

# or
#
#
# change = float(input())
#
# count_coins = 0
# change_coins = change * 100
#
# while True:
#     count_coins += 1
#
#     if change_coins >= 200:
#         change_coins -= 200
#
#     elif change_coins >= 100:
#         change_coins -= 100
#
#     elif change_coins >= 50:
#         change_coins -= 50
#
#     elif change_coins >= 20:
#         change_coins -= 20
#
#     elif change_coins >= 10:
#         change_coins -= 10
#
#     elif change_coins >= 5:
#         change_coins -= 5
#
#     elif change_coins >= 2:
#         change_coins -= 2
#
#     elif change_coins >= 1:
#         change_coins -= 1
#
#     if change_coins < 1:
#         break
#
# print(count_coins)

# or
#

# sum = float(input())
#
# sum = int(sum * 100)
# coins_counter = 0
#
# coins_counter += sum // 200
# sum %= 200
# coins_counter += sum // 100
# sum %= 100
# coins_counter += sum // 50
# sum %= 50
# coins_counter += sum // 20
# sum %= 20
# coins_counter += sum // 10
# sum %= 10
# coins_counter += sum // 5
# sum %= 5
# coins_counter += sum // 2
# sum %= 2
#
# if sum == 1:
#     coins_counter += 1
# print(coins_counter)
#


