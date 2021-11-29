hour = int(input())
day_of_the_week = input()

if hour >= 18 or hour < 10 or day_of_the_week == "Sunday":
    print("closed")
else:
    print("open")

