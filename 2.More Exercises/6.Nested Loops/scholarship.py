import math

income = float(input())
gpa = float(input())
min_wage = float(input())
social = 0.35 * min_wage
excellent = gpa * 25

if gpa >= 5.50:
    if (excellent >= social) or (income > min_wage):
        print(f"You get a scholarship for excellent results {math.floor(excellent)} BGN")
    else:
        print(f"You get a Social scholarship {math.floor(social)} BGN")
elif (income < min_wage) and (gpa > 4.50):
    print(f"You get a Social scholarship {math.floor(social)} BGN")
else:
    print("You cannot get a scholarship!")
