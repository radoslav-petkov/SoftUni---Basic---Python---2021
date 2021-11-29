tickets_number = int(input())

for n in range(tickets_number):
    number_of_ticket = input()


    first_num = number_of_ticket[0]
    second_num = number_of_ticket[1]
    third_num = number_of_ticket[2]
    fourth_num = number_of_ticket[3]

    if len(number_of_ticket) == 4:
        if 'A' <= first_num <= 'Z':
            print(f'Seat decoded: {first_num}{second_num}{third_num}')
        else:
            print(f'Seat decoded: {fourth_num}{second_num}{third_num}')
    elif len(number_of_ticket) == 5 or len(number_of_ticket) == 6:
        ascii_value = ord(second_num)
        print(f"Seat decoded: {first_num}{ascii_value} ")