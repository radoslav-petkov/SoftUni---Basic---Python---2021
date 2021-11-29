number = float(input())
income = input()
outcome = input()

if income == "cm":
    number *=10
elif income == "m":
    number *=1000
if outcome == "cm":
    number /=10
elif outcome == "m":
    number /= 1000

print(f"{number:/3f}")




















