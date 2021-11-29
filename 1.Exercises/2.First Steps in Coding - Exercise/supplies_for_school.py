pens_pack = 5.80
markers_pack = 7.20
cleaner = 1.20

pen_packs_count = int(input())
marker_packs_count = int(input())
cleaner_liters = int(input())
discount = int(input())

marker_packs_price = marker_packs_count * markers_pack
pens_pack_price = pen_packs_count * pens_pack
cleaner_price = cleaner_liters * cleaner
price_sum = marker_packs_price + pens_pack_price + cleaner_price

price_with_discount = price_sum - (price_sum *(discount / 100))

print(price_with_discount )



