holiday_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_profit = puzzles_count * 2.60
dolls_profit = dolls_count * 3
bears_profit = bears_count * 4.10
minions_profit = minions_count * 8.20
trucks_profit = trucks_count * 2

sum = puzzles_profit + dolls_profit + bears_profit + minions_profit + trucks_profit
toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

if toys_count >= 50:
    sum = sum * 0.75

net = sum * 0.90

if net >= holiday_price:
    money_left = net - holiday_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = holiday_price - net
    print(f"Not enough money! {money_needed:.2f} lv needed.")
