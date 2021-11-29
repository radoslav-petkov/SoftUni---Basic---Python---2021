first = input()
second = input()
exception = input()
count = 0
for i in range(ord(first), ord(second) + 1):
    if chr(i) == exception:
        continue
    for j in range(ord(first), ord(second) + 1):
        if chr(j) == exception:
            continue
        for k in range(ord(first), ord(second) + 1):
            if chr(k) == exception:
                continue
            count += 1
            print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
count = str(count)
print("\b", count)
