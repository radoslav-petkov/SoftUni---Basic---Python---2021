import sys

command = input()
max_num = -sys.maxsize

while command != 'Stop':
    number = int(command)

    if number > max_num:
        max_num = number

    command = input()

# if max_number != -sys.maxsize:
#   print (max_number)

print(max_num)

