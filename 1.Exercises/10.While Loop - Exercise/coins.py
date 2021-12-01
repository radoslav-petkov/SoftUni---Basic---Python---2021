change = float(input())

count_coins = 0
change_coins = change * 100

while True:
    count_coins += 1

    if change_coins >= 200:
        change_coins -= 200

    elif change_coins >= 100:
        change_coins -= 100

    elif change_coins >= 50:
        change_coins -= 50

    elif change_coins >= 20:
        change_coins -= 20

    elif change_coins >= 10:
        change_coins -= 10

    elif change_coins >= 5:
        change_coins -= 5

    elif change_coins >= 2:
        change_coins -= 2

    elif change_coins >= 1:
        change_coins -= 1

    if change_coins < 1:
        break

print(count_coins)

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


