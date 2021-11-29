import math

n = int(input())

col_size = math.trunc(n / 2)
mid_size = (2*n - 4 - 2*col_size)

print('/' + '^'*col_size + '\\' + '_'*mid_size + '/' + '^'*col_size + '\\')

for row in range(1, n-1):
    if row == n-2:
        print('|' + ' '*(col_size+1) + '_'*mid_size + ' '*(col_size+1) + '|')
    else:
        print('|{0}|'.format(' '*(n*2-2) ))

print('\\' + '_'*col_size + '/' + ' '*mid_size + '\\' + '_'*col_size + '/')