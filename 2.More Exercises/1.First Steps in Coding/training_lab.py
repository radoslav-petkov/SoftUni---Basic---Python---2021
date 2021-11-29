l = float(input())
w = float(input())
cml = l * 100
cmw = w * 100
result = int(cml / 120) * int((cmw - 100) / 70) - 3
print(result)