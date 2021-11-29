n = int(input())
average_sum = 0

for i in range(n):
    number = int(input())
    average_sum += number / n

print(f"{average_sum:.2f}")
