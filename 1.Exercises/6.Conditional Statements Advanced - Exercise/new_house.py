flowers = input()
flowers_count = int(input())
budget = float(input())
total = 0

if flowers == "Roses":
    if flowers_count > 80:
        total = (flowers_count * 5)*0.9
    else:
        total = flowers_count * 5
if flowers == "Dahlias":
    if flowers_count > 90:
        total = (flowers_count * 3.8)*0.85
    else:
        total = flowers_count * 3.8
if flowers == "Tulips":
    if flowers_count > 80:
        total = (flowers_count * 2.8)*0.85
    else:
        total = flowers_count * 2.8
if flowers == "Narcissus":
    if flowers_count < 120:
        total = flowers_count * 3 + (flowers_count * 3)*0.15
    else:
        total = flowers_count * 3
if flowers == "Gladiolus":
    if flowers_count < 80:
        total = flowers_count * 2.5 + (flowers_count * 2.5)*0.2
    else:
        total = flowers_count * 2.5

if budget >= total:
    print(f"Hey, you have a great garden with {flowers_count} {flowers} and {(budget - total):.2f} leva left.")
elif budget < total:
    print(f"Not enough money, you need {abs(budget - total):.2f} leva more.")