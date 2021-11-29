import math

n = int(input())

middle = math.ceil((2*(n-2)+1)/2)




for row in range(1,middle+1):
    if row == (middle):
        print(' '*(n-1) + '@')
    elif row % 2==0:
        print('-'*(n-2) + '\\' + ' ' + '/' + '-'*(n-2))
    elif row %2!=0:
        print('*'*(n-2) + '\\' + ' ' + '/' + '*'*(n-2))

for row in range(1, middle):
    if row%2 == 0:
        print('-'*(n-2) + '/' + ' ' + '\\' + '-'*(n-2))
    else:
        print('*'*(n-2) + '/' + ' ' + '\\' + '*'*(n-2))