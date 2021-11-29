budget = int (input ())
command = input ()
while command != "Stop":
    current_price = 0
    for letter in command:
        current_price += ord(letter)

    if budget >= current_price:
        budget -= current_price
        print ("Item successfully purchased!")
    else:

        print ("Not enough money!")
        break
    command = input()

if command ==  "Stop":
    print (f"Money left: {budget}")

