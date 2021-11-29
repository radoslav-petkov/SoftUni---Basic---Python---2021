month = input()
hours = int(input())
people = int(input())
day_night = input()
price = 0
total_cost = 0

if day_night == 'day' and month in ['march', 'april', 'may']:
    price = 10.5
    if people > 3:
        price *= 0.9
    if hours > 4:
        price *= 0.5
elif day_night == 'day' and month in ['june', 'july', 'august']:
    price = 12.6
    if people > 3:
        price *= 0.9
    if hours > 4:
        price *= 0.5
elif day_night == 'night' and month in ['march', 'april', 'may']:
    price = 8.4
    if people > 3:
        price *= 0.9
    if hours > 4:
        price *= 0.5
elif day_night == 'night' and month in ['june', 'july', 'august']:
    price = 10.2
    if people > 3:
        price *= 0.9
    if hours > 4:
        price *= 0.5

total_cost = price * hours * people

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total_cost:.2f}')
#
# or
#
# month = input()  # "march", "april", "may", "june", "july", "august"
# hours = int(input())
# group_size = int(input())
# time_of_the_day = input()  # "day", "night"
#
# price_per_hour_per_person = 0
# total = 0
#
# if time_of_the_day == 'day':
#     if month in ["march","april","may"]:
#         price_per_hour_per_person = 10.50
#     elif month in ["june","july","august"]:
#         price_per_hour_per_person = 12.60
# elif time_of_the_day == 'night':
#     if month in ["march","april","may"]:
#         price_per_hour_per_person = 8.40
#     elif month in ["june","july","august"]:
#         price_per_hour_per_person = 10.20
#
# if group_size > 3:
#     price_per_hour_per_person *= 0.9
#
# if hours > 4:
#     price_per_hour_per_person *= 0.5
#
# total = group_size * hours * price_per_hour_per_person
#
# print(f'Price per person for one hour: {price_per_hour_per_person:.2f}')
# print(f'Total cost of the visit: {total:.2f}')