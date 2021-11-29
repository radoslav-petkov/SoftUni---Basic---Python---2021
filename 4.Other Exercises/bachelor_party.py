money_for_singer = int(input())

income = 0
command =  input()

while command != "The restaurant is full":
    num_of_people = int (command)
    if num_of_people < 5:
        income += 100 * num_of_people
    else:
        income += 70 * num_of_people
    total_guests += num_of_people
    command = input()
if income >= money_for_singer:
    print (f'You have {total_guests} guests and {income - money_for_singer} leva left.')
else:
    print (f"You have (total guests} guests and {income} leva income, but no singer.")



