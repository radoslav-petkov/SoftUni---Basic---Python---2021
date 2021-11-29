from math import floor

count_balls = int(input())

total_points = 0
count_red  = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_others = 0
count_black = 0


for ball in range(1, count_balls + 1):
    color = input()
    if color == "red":
        total_points += 5
        count_red += 1

    elif color == "orange":
        total_points += 10
        count_orange += 1

    elif color == "yellow":
        total_points += 15
        count_yellow += 1

    elif color == "white":
        total_points += 20
        count_white += 1

    elif color == "black":
        total_points /= 2
        count_black += 1
    else:
        count_others += 1

print(f"Total points: {floor(total_points)}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_others}")
print(f"Divides from black balls: {count_black}")














