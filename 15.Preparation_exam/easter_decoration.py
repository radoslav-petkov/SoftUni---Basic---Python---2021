number_of_customers = int(input())

total_money = 0

for current_customer in range(number_of_customers):

    current_sum = 0
    number_of_purchases = 0

    command = input()
    while command != "Finish":
        current_product = command
        number_of_purchases += 1

        if current_product == "basket":
            current_sum += 1.50

        elif current_product == "wreath":
            current_sum += 3.80

        elif current_product == "chocolate bunny":
            current_sum += 7

        command = input()

    if number_of_purchases % 2 == 0:
        current_sum *= 0.80   # current_sum = current-sum - current_sum + 0.20
    print(f"You purchased {number_of_purchases} items for {current_sum:.2f} leva.")

    total_money += current_sum

average_money = total_money / number_of_customers
print(f"Average bill per client is: {average_money:.2f} leva.")