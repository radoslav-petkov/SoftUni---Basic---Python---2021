customers = int(input())
basket = 1.50
wreath = 3.80
chocolate_bunny = 7.00
total = 0
average_money = 0
current_client_sum = 0
count = 0

for i in range(customers):
    command = input()

    while command != "Finish":
        if command == "basket":
            count += 1
            current_client_sum += basket
        elif command == "wreath":
            count += 1
            current_client_sum += wreath
        elif command == "chocolate bunny":
            count += 1
            current_client_sum += chocolate_bunny
        command = input()

    if count % 2 == 0:
        current_client_sum *= 0.80
    if command == "Finish":
        print(f"You purchased {count} items for {current_client_sum:.2f} leva.")
    total += current_client_sum
    count = 0
    current_client_sum = 0

average_money = total / customers
print(f"Average bill per client is: {average_money:.2f} leva.")

