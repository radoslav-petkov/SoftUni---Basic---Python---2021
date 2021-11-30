k - int(input())
l = int(input())
m - int(input())
n - int(input())

for number_1 in range(k, 8+1):
     for number_2 in range(9, 1-1, -1):
           for number_3 in range(m, 8+1):
                for number_4 in range(9, n-1, -1):
                     if (number_1 % 2 == 0 and not number_2 % 2 == 0) and (number_3 % 2 == 0 and not number_4 % 2 == 0):
                          if not number_1 == number_3 and not number_2 == number_4:
                              print(f"{number_1}{number_2} - {number_3}{number_4}")
                          else:
                               print("Cannot change the same player.")
