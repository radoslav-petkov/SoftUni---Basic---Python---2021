fruit = input()
size_per_set = input()
order_sets = int(input())

cost = 0

if fruit == "Watermelon":
    if size_per_set == "small":
        cost = (2 * 56) * order_sets
    if size_per_set == "big":
        cost = (5 * 28.70) * order_sets

elif fruit == "Mango":
    if size_per_set == "small":
        cost = (2 * 36.66) * order_sets
    if size_per_set == "big":
        cost = (5 * 19.60) * order_sets

elif fruit == "Pineapple":
    if size_per_set == "small":
        cost = (2 * 42.10) * order_sets
    if size_per_set == "big":
        cost = (5 * 24.80) * order_sets

elif fruit == "Raspberry":
    if size_per_set == "small":
        cost = (2 * 20) * order_sets
    if size_per_set == "big":
        cost = (5 * 15.20) * order_sets

if 400 <= cost <= 1000:
    cost -= cost * 0.15
elif cost > 1000:
    cost -= cost * 0.50

print(f"{cost:.2f} lv.")








