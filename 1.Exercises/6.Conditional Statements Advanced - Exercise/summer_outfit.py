temperature = int(input())
part_of_the_day = input()

outfit = "Shirt"
shoes = "Moccasins"

if part_of_the_day == "Morning":
    if 10 <= temperature <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif temperature >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif part_of_the_day == "Afternoon":
    if temperature >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif temperature > 18:
        outfit = "T-Shirt"
        shoes = "Sandals"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")