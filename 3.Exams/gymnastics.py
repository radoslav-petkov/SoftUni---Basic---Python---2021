country = input()
instrument = input()

total_grade = 0

if country == "Russia":
   if instrument == "ribbon":
       total_grade = 9.1 + 9.4
   elif instrument == "hoop":
        total_grade = 9.3 + 9.8
   elif instrument == "rope":
        total_grade = 9.6 + 9

elif country == "Bulgaria":
    if instrument == "ribbon":
        total_grade = 9.6 + 9.4
    elif instrument == "hoop":
        total_grade = 9.55 + 9.75
    elif instrument == "rope":
        total_grade = 9.5 + 9.4

elif country == "Italy":
    if instrument == "ribbon":
        total_grade = 9.2 + 9.5
    elif instrument == "hoop":
        total_grade = 9.45 + 9.35
    elif instrument == "rope":
        total_grade = 9.7 + 9.15

print(f"The team of {country} get {total_grade:.3f} on {instrument}.")

need_grade = 20 - total_grade
need_percent = (need_grade / 20) * 100
print(f"{need_percent:.2f}%")











