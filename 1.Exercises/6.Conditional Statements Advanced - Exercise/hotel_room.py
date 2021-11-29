month = input()
number_of_nights = int(input())
costs_for_apartment = 0
costs_for_studio = 0

if month == "May" or month == "October":
    costs_for_apartment = 65 * number_of_nights
    costs_for_studio = 50 * number_of_nights

    if 7 < number_of_nights <= 14:
        costs_for_studio -= costs_for_studio * 0.85
    if number_of_nights > 14:
        costs_for_studio -= costs_for_studio * 0.30
        costs_for_apartment -= costs_for_apartment * 0.10

elif month == "June" or month == "September":
    costs_for_apartment == 68.70 * number_of_nights
    costs_for_studio == 75.20 * number_of_nights

    if number_of_nights > 14:
        costs_for_studio -= costs_for_studio * 0.30
        costs_for_apartment -= costs_for_apartment * 0.10

elif month == "July" or month == "August":
    costs_for_apartment = 77 * number_of_nights
    costs_for_studio = 76 * number_of_nights

    if number_of_nights > 14:
        costs_for_apartment -= costs_for_apartment * 0.10

print(f"Apartment: {costs_for_apartment:.2f} lv.")
print(f"Studio: {costs_for_studio:.2f} lv.")



































