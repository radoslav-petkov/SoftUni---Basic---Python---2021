import sys

command = input()
min_number = sys.maxsize

while command != "Stop":
    current_number = int(command)

    if current_number < min_number:
        min_number = current_number

    command = input ()

# if min_number != sys.maxsize:
#   print (min_number)

print(min_number)
