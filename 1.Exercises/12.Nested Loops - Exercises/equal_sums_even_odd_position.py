first_num = int(input())
second_num = int(input())
for number in range (first_num, second_num + 1):
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate (str(number)):
        if (index + 1) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print (number, end=' ')



#
# or


#
# n1 = int(input())
# n2 = int(input())
# odd_nums = 0
# even_nums = 0
#
# for num in range(n1, n2 + 1):
#     current_num = str(num)
#
#     for x in range(len(current_num)):
#         if x % 2 == 0:
#             even_nums += int(current_num[x])
#         else:
#             odd_nums += int(current_num[x])
#
#     if even_nums == odd_nums:
#         print(current_num, end= " ")
#     odd_nums = 0
#     even_nums = 0
