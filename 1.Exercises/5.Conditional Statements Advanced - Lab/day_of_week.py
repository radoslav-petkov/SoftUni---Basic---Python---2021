number = int(input())

if 1 <= number <= 7:    # [1:7]
    if number == 1:
        print("Monday")
    if number == 2:
        print("Tuesday")
    if number == 3:
        print("Wednesday")
    if number == 4:
        print("Thursday")
    if number == 5:
        print("Friday")
    if number == 6:
        print("Saturday")
    if number == 7:
        print("Sunday")
else:
    print("Error")