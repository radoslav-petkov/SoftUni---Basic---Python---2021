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