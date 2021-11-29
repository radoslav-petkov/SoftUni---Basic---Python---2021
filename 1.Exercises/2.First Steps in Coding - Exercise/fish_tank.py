length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_tank = length * width * height
volume_litres = volume_tank / 1000
occupied_space = percent / 100
req_litres = volume_litres * (1 - occupied_space)

print(req_litres)
















