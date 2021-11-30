month = input().lower()
hours = int(input())
people = int(input())
day_or_nigth = input()

result = 0

if month == "march" or month == "april" or month == "may":
  if day_or_nigth == "day":
     result = 10.50
  else:
     result = 8.40

elif month == "june" or month == "july" or month == "august":
  if day_or_night == "day":
     result = 12.60
  else:
     result = 10.20

if people >= 4:
   result = result * 0.90
if hours >= 5 :
   result = result - result * 0.50

sum =  result * people * hours

print(f"Price per person for one hour: {result:.2f}")
print(f"Total cost of the visit: {sum:.2f}")