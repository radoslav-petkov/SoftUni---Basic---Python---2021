total_sum = 0
command = input()

while command != "NoMoreMoney":
    current_number = float(command)

    if current_number < 0:
        print("Invalid operation!")
        break

    total_sum += current_number
    print(f"Increase: {current_number:.2f}")

    command = input()

print(f"Total: {total_sum:.2f}")

