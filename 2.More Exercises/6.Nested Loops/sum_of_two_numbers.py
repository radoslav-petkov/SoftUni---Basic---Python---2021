start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combinations_counter = 0
combination_number_found = False

for first_num in range(start_interval, end_interval+1):
    for second_num in range(start_interval, end_interval+1):
        combinations_counter +=1

        if first_num + second_num == magic_number:
            print(f'Combination N:{combinations_counter} ({first_num} + {second_num} = {magic_number})')
            combination_number_found = True
            break
    if combination_number_found:
        break
if not combination_number_found:
    print(f'{combinations_counter} combinations - neither equals {magic_number}')