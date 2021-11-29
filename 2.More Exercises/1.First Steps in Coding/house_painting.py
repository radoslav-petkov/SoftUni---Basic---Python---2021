x = float(input())
y = float(input())
h = float(input())

# needed green paint
front = x * x - 2 * 1.2
back = x * x
aside = 2 * (x * y - 1.5 * 1.5)
total_metres_green = front + back + aside
green_paint = total_metres_green / 3.4

# needed red paint
sides = 2 * x * y
triangles = x * h
total_metres_red = sides + triangles
red_paint = total_metres_red / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")



#print(round(green_paint, 2))
#print(round(red_paint, 2))


#print("*" + "int(input()) + "*")

#print(f"{area:.2f}")
#print(format(area, ".2f"))








