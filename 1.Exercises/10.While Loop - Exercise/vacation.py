need_money = float(input())
current_money = float(input())

count_spend_days = 0
count_days = 0

while current_money < need_money:
    action = input()
    count_days += 1
    sum = float(input())

    if action == "spend":
        count_spend_days += 1
        current_money -= sum
        if current_money < 0:
            current_money = 0

    elif action == "save":
        count_spend_days = 0
        current_money += sum

    if count_spend_days == 5:
        print("You can't save the money.")
        print(count_days)
        break

else:
    print(f"You saved the money for {count_days} days.")

#
# or
#
# needed_money = float(input())
# money_in_hand = float(input())
#
# spending_days_counter = 0
# spending_too_many_days = False
# total_days = 0
#
# while money_in_hand < needed_money:
#     action = input()
#     sum = float(input())
#     total_days += 1
#
#     if action == "spend":
#         money_in_hand -= sum
#         if money_in_hand < 0:
#             money_in_hand = 0
#         spending_days_counter += 1
#         if spending_days_counter == 5:
#             spending_too_many_days = True
#             break
#     else:
#         money_in_hand += sum
#         spending_days_counter = 0
#
# if spending_too_many_days: #if spending_too_many_days == True
#     print("You can't save the money.")
#     print(total_days)
# else:
#     print(f"You saved the money for {total_days} days.")
