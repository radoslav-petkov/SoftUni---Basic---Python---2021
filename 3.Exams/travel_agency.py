town = input()
packet = input()
vip = input()
days = int(input())
towns = ("Bansko", "Borovets", "Varna", "Burgas")
packets = ("withEquipment", "noEquipment", "withBreakfast", "noBreakfast")

if town not in towns or packet not in packets:
    print("Invalid input!")
    quit()

if days < 1:
    print("Days must be positive number!")
    quit()

if days > 7:
    days -= 1
else:
    days = days

if town == "Bansko" or town == "Borovets":
    if packet == "withEquipment":
        price = days * 100
    elif packet == "noEquipment":
        price = days * 80

if vip == "yes" and packet == "withEquipment":
    price *= 0.90
elif vip == "yes" and packet == "noEquipment":
    price *= 0.95

if town == "Varna" or town == "Burgas":
    if packet == "withBreakfast":
        price = days * 130
    elif packet == "noBreakfast":
        price = days * 100

if vip == "yes" and packet == "withBreakfast":
    price *= 0.88
elif vip == "yes" and packet == "noBreakfast":
    price *= 0.93

print(f"The price is {price:.2f}lv! Have a nice time!")