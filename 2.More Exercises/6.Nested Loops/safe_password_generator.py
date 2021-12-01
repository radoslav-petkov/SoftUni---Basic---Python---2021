third_symbol = int(input())
fourth_symbol = int(input())
max_combinations = int(input())
total_combinations = 0
first_and_last_symbol = 35
second_and_before_last_symbol = 64

for i in range(1,third_symbol + 1):
    for x in range(1,fourth_symbol + 1):
        total_combinations += 1
        if total_combinations > max_combinations:
            break
        if first_and_last_symbol > 55:
            first_and_last_symbol = 35
        if second_and_before_last_symbol > 96:
            second_and_before_last_symbol = 64
        print(
            f"{chr(first_and_last_symbol)}{chr(second_and_before_last_symbol)}{i}{x}{chr(second_and_before_last_symbol)}{chr(first_and_last_symbol)}",
            end = "|")
        first_and_last_symbol += 1
        second_and_before_last_symbol += 1
