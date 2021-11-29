from math import ceil, floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

sum = (magnolias * 3.25) + (hyacinths * 4) + (roses * 3.5) + (cactuses * 8)
taxes = 0.05 * sum
net = sum - taxes

if net >= gift_price:
    needed_money = floor(net - gift_price)
    print(f"She is left with {needed_money} leva.")
else:
    left_money = ceil(gift_price - net)
    print(f"She will have to borrow {left_money} leva.")

