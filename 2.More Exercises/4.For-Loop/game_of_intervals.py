entry = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p_inv = 0
total_result = 0

for i in range(0, entry):
    number = int(input())
    if number >= 0 and number <= 50:
        if 0 <= number <= 9:
            number *= 0.2
            p1 += 1
        elif 10 <= number <= 19:
            number *= 0.3
            p2 += 1
        elif 20 <= number <= 29:
            number *= 0.4
            p3 += 1
        elif 30 <= number <= 39:
            number = 50
            p4 += 1
        elif 40 <= number <= 50:
            number = 100
            p5 += 1
        total_result += number
    else:
        total_result /= 2
        p_inv += 1

print(f"{total_result:.2f}")
print(f"From 0 to 9: {p1 / entry * 100:.2f}%")
print(f"From 10 to 19: {p2 / entry * 100:.2f}%")
print(f"From 20 to 29: {p3 / entry * 100:.2f}%")
print(f"From 30 to 39: {p4 / entry * 100:.2f}%")
print(f"From 40 to 50: {p5 / entry * 100:.2f}%")
print(f"Invalid numbers: {p_inv / entry * 100:.2f}%")

