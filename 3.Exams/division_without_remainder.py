num_count = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1, num_count + 1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2t += 1
    if number % 4 == 0:
        p3 += 1

print(f'{p1 / num_count * 100:.2f}%')
print(f'{p2 / num_count * 100:.2f}%')
print(f'{p3 / num_count * 100:.2f}%')