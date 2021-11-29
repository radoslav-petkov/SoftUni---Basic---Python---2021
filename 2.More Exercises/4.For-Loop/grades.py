students = int(input())

p2_3 = 0
p3_4 = 0
p4_5 = 0
p5 = 0
average_grade = 0

for i in range(1, students+1):
    grade = float(input())

    if grade >= 5.00:
        p5 += 1
    if 4.00 <= grade <= 4.99:
        p4_5 += 1
    if 3.00 <= grade <= 3.99:
        p3_4 += 1
    if grade < 3.00:
        p2_3 += 1

    average_grade += grade / students

print(f"Top students: {p5 / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {p4_5 / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {p3_4 / students * 100:.2f}%")
print(f"Fail: {p2_3 / students * 100:.2f}%")
print(f"Average: {average_grade:.2f}")




