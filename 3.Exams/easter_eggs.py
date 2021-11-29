number_of_red_eggs = 0
number_of_orange_eggs = 0
number_of_blue_eggs = 0
number_of_green_eggs = 0
number_of_max_eggs_from_same_color = 0
color_of_max_eggs = ""
number_of_eggs = int(input())
for eggs in range(number_of_eggs):
    color_of_current_egg = input()

    if color_of_current_egg == "red":
        number_of_red_eggs += 1
        if number_of_red_eggs > number_of_max_eggs_from_same_color:
            color_of_max_eggs = "red"
            number_of_max_eggs_from_same_color = number_of_red_eggs

    elif color_of_current_egg == "orange":
        number_of_orange_eggs += 1
        if number_of_orange_eggs > number_of_max_eggs_from_same_color:
            color_of_max_eggs = "orange"
            number_of_max_eggs_from_same_color = number_of_orange_eggs

    elif color_of_current_egg == "blue":
        number_of_blue_eggs += 1
        if number_of_blue_eggs > number_of_max_eggs_from_same_color:
            color_of_max_eggs = "blue"
            number_of_max_eggs_from_same_color = number_of_blue_eggs

    elif color_of_current_egg == "green":
        number_of_green_eggs += 1
        if number_of_green_eggs > number_of_max_eggs_from_same_color:
            color_of_max_eggs = "green"
            number_of_max_eggs_from_same_color = number_of_green_eggs

print(f"Red eggs: {number_of_red_eggs}")
print(f"Orange eggs: {number_of_orange_eggs}")
print(f"Blue eggs: {number_of_blue_eggs}")
print(f"Green eggs: {number_of_green_eggs}")
print(f"Max eggs: {number_of_max_eggs_from_same_color} -> {color_of_max_eggs}")







