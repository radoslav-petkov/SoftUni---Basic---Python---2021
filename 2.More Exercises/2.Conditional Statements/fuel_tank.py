type_of_fuel = input()
litres_fuel = float(input())

if type_of_fuel in ("Diesel Gasoline Gas") and litres_fuel >= 25:
    print(f"You have enough {type_of_fuel.lower()}.")
elif type_of_fuel in ("Diesel Gasoline Gas") and litres_fuel < 25:
    print(f"Fill your tank with {type_of_fuel.lower()}!")

else:
    print("Invalid fuel!")