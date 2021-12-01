control_number = int(input())
cnt = 0
pa = 0
pb = 0
pc = 0
pd = 0
counter = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if 4 <= control_number <=144:
                 if control_number == a * b + c * d and a < b and c > d:

                    cnt += 1
                    if cnt == 4:
                        counter = True

                        pa = a
                        pb = b
                        pc = c
                        pd = d

                    print(f"{a}{b}{c}{d}", end=" ")

if counter:
    print()
    print(f"Password: {pa}{pb}{pc}{pd}")

else:
    print()
    print("No!")