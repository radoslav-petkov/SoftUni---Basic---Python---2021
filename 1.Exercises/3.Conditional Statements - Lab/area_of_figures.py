from math import pi

figure = str(input())

if figure == 'square':
    a = float(input())
    s = a * a
    print(f"{s:.3f}")

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    s = a * b
    print(f"{s:.3f}")

elif figure == 'circle':
    r = float(input())
    s = pi * r * r
    print(f"{s:.3f}")

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    s = a * h / 2
    print(f"{s:.3f}")