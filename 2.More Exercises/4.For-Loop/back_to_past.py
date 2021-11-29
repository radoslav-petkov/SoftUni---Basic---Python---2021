budget = float(input())
year = int(input())
age = 18
for years in range(1800, year + 1):
    if years % 2 == 0:
        budget -= 12000
    else:
        budget -= 12000 + 50 * age
    age += 1
if budget >= 0:
    print(f'Yes! He will live a carefree life and will have {budget:.2f} dollars left.')
else:
    print(f"He will need {abs(budget):.2f} dollars to survive.")