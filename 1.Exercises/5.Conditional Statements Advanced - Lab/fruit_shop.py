fruit = input()
week_day = input()
quantity = float(input())
price = 0

if week_day == 'Monday' \
        or week_day == 'Tuesday' \
        or week_day == 'Wednesday' \
        or week_day == 'Thursday' \
        or week_day ==  'Friday':
    if fruit == 'banana':
        price = 2.5
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85

elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'banana':
        price = 2.7
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.6
    elif fruit == 'kiwi':
        price = 3
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2


if price == 0:
    print('error')
else:
    total_price = quantity * price
    print(f'{total_price:.2f}')


    #or

# fruit = input()
# day_of_the_week = input()
# quantity = float(input())
# price = 0

# fruit_is_valid = True
# day_of_the_week_is_valid = True

# if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday' or day_of_the_week == 'Friday':
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#     else:
#         fruit_is_valid = False
# elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#     else:
#         fruit_is_valid = False
# else:
#     day_of_the_week_is_valid = False
# if day_of_the_week_is_valid and fruit_is_valid: #day_of_the_week_is_valid == True and fruit_is_valid == True
#     price *= quantity  #price = price * quantity
#     print(f"{price:.2f}")
# else:
#     print("error")