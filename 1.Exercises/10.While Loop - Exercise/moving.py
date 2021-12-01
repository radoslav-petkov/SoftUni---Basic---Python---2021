width = int(input())
length = int(input())
heigth = int(input())

there_is_more_free_space = True
total_free_space = width * length * heigth
command = input()

while command != "Done":
    number_of_boxes = int(command)
    total_free_space -= number_of_boxes
    if total_free_space < 0:
        there_is_more_free_space = False
        break
    command = input()
if there_is_more_free_space:
    print(f"{total_free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")

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