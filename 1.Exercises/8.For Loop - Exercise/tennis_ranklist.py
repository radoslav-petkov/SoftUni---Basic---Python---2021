from math import floor

tournaments_count = int(input())
initial_points = int(input())

W = 2000
f = 1200
sf = 720
points = 0
winner = 0

for tournament in range (tournaments_count):
    stage = input()

    if stage == "W":
        points += w
        winner += 1
    elif stage == "F":
        points += f
    elif stage == "SF":
        points += sf

average_points = floor(points / tournaments_count)
win_percent = winner / tournaments_count * 100
final_points = initial_points + points

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")