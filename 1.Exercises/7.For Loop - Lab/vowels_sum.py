text = input()
points = 0

for letter in text:
    if letter == "a":
        points += 1
    elif letter == "e":
        points += 2
    elif letter == "i":
        points += 3
    elif letter == "o":
        points += 4
    elif letter == "u":
        points += 5
print(points)
