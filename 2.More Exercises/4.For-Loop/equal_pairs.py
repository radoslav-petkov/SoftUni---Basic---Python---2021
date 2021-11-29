import sys

pairs_of_nums = int(input())

value = 0
difference = -sys.maxsize
is_different = False

for i in range(pairs_of_nums):
    first_pair = int(input())
    second_pair = int(input())

    sum_of_pairs = first_pair + second_pair
    if i == 0:
        value = sum_of_pairs
    else:
        if value != sum_of_pairs:
            difference = abs(sum_of_pairs - value)
            is_different = True
            value = sum_of_pairs
if is_different:
    print(f"No, maxdiff={difference}")
else:
    print(f"Yes, value={value}")