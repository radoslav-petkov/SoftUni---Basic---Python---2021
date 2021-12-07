budget = int(input())
n = int(input())

total_amount = 0

for item in range(0, n):
    input_item = input()

    if 'hoodie' == input_item:
        total_amount += 30
    elif 'keychain'== input_item:
        total_amount += 4
    elif 'T-shirt' == input_item:
        total_amount += 20
    elif 'flag' == input_item:
        total_amount += 15
    elif 'sticker' == input_item:
        total_amount += 1

diff = abs(total_amount - budget)

if total_amount <= budget:
    print(f"You bought {n} items and left with {diff} lv.")
else:
    print(f"Not enough money, you need {diff} more lv.")