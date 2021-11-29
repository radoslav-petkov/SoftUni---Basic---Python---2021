season = input()
type_of_group = input()
student_count = int(input())
sleepovers_count = int(input())
price = 0
sport = 0

if season == "Winter":
    if type_of_group in "boys girls":
        price = student_count * sleepovers_count * 9.60
    elif type_of_group == "mixed":
        price = student_count * sleepovers_count * 10

elif season == "Spring":
    if type_of_group in "boys girls":
        price = student_count * sleepovers_count * 7.20
    elif type_of_group == "mixed":
        price = student_count * sleepovers_count * 9.50

elif season == "Summer":
    if type_of_group in "boys girls":
        price = student_count * sleepovers_count * 15
    elif type_of_group == "mixed":
        price = student_count * sleepovers_count * 20


if student_count >= 50:
            price -= price * 0.50
elif 20 <= student_count < 50:
            price -= price * 0.15
elif 10 <= student_count < 20:
            price -= price * 0.05


if season == "Winter":
    if type_of_group == "girls":
        sport = "Gymnastics"
    elif type_of_group == "boys":
        sport = "Judo"
    elif type_of_group == "mixed":
        sport = "Ski"

elif season == "Spring":
    if type_of_group == "girls":
        sport = "Athletics"
    elif type_of_group == "boys":
        sport = "Tennis"
    elif type_of_group == "mixed":
        sport = "Cycling"

elif season == "Summer":
    if type_of_group == "girls":
        sport = "Volleyball"
    elif type_of_group == "boys":
        sport = "Football"
    elif type_of_group == "mixed":
        sport = "Swimming"


print(f"{sport} {price:.2f} lv.")


















