int(input())
counter = 0

for name_s in range(ord('B'), ord('L')+1, 2):
    for sektor in range(ord('f'), ord('a')-1, -1):
        for entrance in range(ord('A'), ord('C') + 1):
            for row_num in range(1, 11):
                for seat in range(10, 0, -1):
                     counter += 1

                     if counter == n:
                         sum = name_s + sektor + entrance + row_num + seat
                         print(f"Ticket combination: {chr(name_s)}{chr(sektor)}{chr(entrance)}{row_num}{seat}")
                         print(f"Prize: {sum} lv.")