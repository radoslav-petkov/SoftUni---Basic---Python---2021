chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegan_menu_count = int(input())

chicken_menu_price_sum = chicken_menu_count * chicken_menu_price
fish_menu_price_sum = fish_menu_count * fish_menu_price
vegan_menu_price_sum = vegan_menu_count * vegan_menu_price

menus_sum = chicken_menu_price_sum + fish_menu_price_sum + vegan_menu_price_sum
desert_price = (20 / 100) * menus_sum

order_price_sum = menus_sum + desert_price + 2.50

print(order_price_sum)












