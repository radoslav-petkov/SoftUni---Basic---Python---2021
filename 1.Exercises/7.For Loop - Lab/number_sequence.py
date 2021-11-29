import sys

n = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range (n):
    number = int(input())
    if number > max_number:
        max_number = number

    if number < min_number:
       min_number = number

print(f'Max number: {max_number}')
print(f'Min number: {max_number}')

# or
#
# count_of_numbers int(input())
# first_number = int(input())
# min_number = first_number
# max_number = first_number
# for numbers in range (count of_numbers - 1):
#     number = int(input())
#     if number > max_number:
#         max_number = number
#     if number < min_number:
#         min_number = number
# print (f"Max number: {max_number}")
# print(f"Min number: {min_number}")
