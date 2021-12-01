w = int(input())
l= int(input())
h = int(input())

free_space = w * l * h

while True:
    box = input()
    if box == "Done":
        print(f"{free_space} Cubic meters left.")
        break

    free_space -= int(box)

    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
        
        
#     or
#
# width = int(input())
# length = int(input())
# height = int(input())
# free_box_space = width * length * height
#
# operator = input()
# needed_cubic = 0
#
# while True:
#     if operator == "Done":
#         print(f"{free_box_space} Cubic meters left.")
#         break
#     else:
#         operator_int = int(operator)
#         free_box_space -= operator_int
#         if free_box_space <= 0:
#             print(f"No more free space! You need {abs(free_box_space)} Cubic meters more.")
#             break
#         else:
#             operator = input()
