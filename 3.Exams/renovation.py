import math
height = int(input())
width = int(input())
# 10% -> 0.1
# 5% -> 0.05
paint_free_percent = int(input()) / 100
# Calculate total area to be painted
total_paint_area = 4 * height * width
total_paint_area -= total_paint_area * paint_free_percent
total_paint_area = math.ceil(total_paint_area)
command = input()
while command != 'Tired!':
    paint_liters = int(command)
    paint_liters = int(command)
    # Paint the wall
    total_paint_area -= paint_liters
    if total_paint_area <= 0:
        # All walls are painted successfully
        break
    # EV
    command = input()

if total_paint_area > 0:
    # We are tired and we have not succeeded to paint the walls
    print(f'{total_paint_area} quadratic m left.')
elif total_paint_area == 0:
    print(f'All walls are painted! Great job, Pesho!')
else:
    print(f'All walls are painted and you have {abs(total_paint_area)} l paint left!')