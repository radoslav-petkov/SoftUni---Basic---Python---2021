season = input()
distance_month = float(input())
sum = 0

if distance_month <= 5000:
    if season in "Spring Autumn":
        sum = distance_month * 0.75
    if season == "Summer":
        sum = distance_month * 0.90
    if season == "Winter":
        sum = distance_month * 1.05

if 5000 < distance_month <= 10000:
    if season in "Spring Autumn":
        sum = distance_month * 0.95
    if season == "Summer":
        sum = distance_month * 1.10
    if season == "Winter":
        sum = distance_month * 1.25

if 10000 < distance_month <= 20000:
    if season in "Spring Autumn":
        sum = distance_month * 0.95
    if season == "Summer":
        sum = distance_month * 1.10
    if season in "Spring Summer Autumn Winter":
        sum = distance_month * 1.45

sum_after_tax = sum * 4 * 0.9

print(f"{sum_after_tax:.2f}")





















