count_bottles = int(input())
detergent = 750 * count_bottles
plates = 0
pots = 0
counter = 0

while detergent >= 0:
    command = input()

    if command == 'End':
        break

    dishes = int(command)

    counter += 1

    if counter % 3 == 0:
        pots += dishes
        detergent -= dishes * 15
    else:
        plates += dishes
        detergent -= dishes * 5

if detergent < 0:
    print(f"Not enough detergent, {-detergent} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")