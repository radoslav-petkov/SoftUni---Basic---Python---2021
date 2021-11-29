mackerel = float(input())
sprat = float(input())
bonito_price_kg = float(input())
scad_price_kg = float(input())
mussels_price_kg = int(input())


bonito_price = mackerel * 1.6
bonito_total_sum = bonito_price * bonito_price_kg

scad_price = sprat * 1.8
scad_total_sum = scad_price * scad_price_kg

mussels_total_sum = 7.5 * mussels_price_kg

total_sum = bonito_total_sum + scad_total_sum + mussels_total_sum

print(f"{total_sum:.2f}")