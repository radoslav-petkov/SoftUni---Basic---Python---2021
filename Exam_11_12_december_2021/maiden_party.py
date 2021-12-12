price_women_party = float(input())
love_letters = int(input())
wax_roses = int(input())
keychains = int(input())
caricatures = int(input())
fortunes_suprises = int(input())

discount = 0
total_sum = 0

sum = love_letters * 0.6 + wax_roses * 7.20 + keychains * 3.60 + caricatures * 18.20 + fortunes_suprises * 22
articules_count = love_letters + wax_roses + keychains + caricatures + fortunes_suprises

if articules_count > 25:
   discount = sum - sum * 0.65

total_sum = (sum - discount)
net = total_sum - (0.1 * total_sum)

if net > price_women_party:
    money_left = net - price_women_party
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_need = price_women_party - net
    print(f"Not enough money! {money_need:.2f} lv needed.")


