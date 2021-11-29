sweet_bread = int(input())
eggs_board = int(input())
cookie = int(input())

eggs_paint = eggs_board * 12
sweet_bread_price = sweet_bread * 3.2

eggs_price = eggs_board * 4.35
cookies_price = cookie * 5.4
egg_paint_price = eggs_paint * 0.15

total_price = sweet_bread_price + eggs_price + cookies_price + egg_paint_price
print(f"{total_price:.2f}")