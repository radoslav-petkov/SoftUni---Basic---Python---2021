n = int(input())

left_sum = 0
right_sum = 0

for i in range (n):
 number = int(input ())
 left_sum += number

for j in range (n):
 number = int(input())
 right_sum += number

if left_sum == right_sum:
 print(f'Yes, sum = {left_sum}')
else:
 print(f'No, diff = {abs(left_sum - right_sum)}')


 #
 # or
 #


 # n = int(input())
 # left_sum = 0
 # right_sum = 0
 # for number in range(0, n*2):
 #     current_num = int(input())
 #     if number < n:
 #         left_sum+=current_num
 #     elif number >=n:
 #         right_sum+=current_num
 #
 # if left_sum == right_sum:
 #     print('Yes, sum = ' + str(right_sum))
 # else:
 #     diff = abs(left_sum-right_sum)
 #     print('No, diff = '+ str(diff))
 #
 #
 # # or