a = int(input())
b = int(input())
c = int(input())
for i in range(1, a+1):
	if i % 2 == 0:
		for j in range(2, b+1):
			if j == 2 or j == 3 or j == 5 or j == 7:
				for k in range(1, c+1):
					if k % 2 == 0:
						print(f'{i} {j} {k}')