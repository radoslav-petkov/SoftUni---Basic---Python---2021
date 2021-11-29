pass
pass
count_products = 0
sum = 0
while product != "Stop":
    price = float (input())
    count_products += 1
    if count_products % 3 == 0:
        sum += price / 2
    else:
        sum += price
    if sum > budget:
       print ("You don't have enough money!")
        need_money = sum - budget
        print(f"You need {need_money: .2f} leva!")
        break
    product = input()
else:
   print (f"You bought {count_products} products for {sum: .2f} leva.")