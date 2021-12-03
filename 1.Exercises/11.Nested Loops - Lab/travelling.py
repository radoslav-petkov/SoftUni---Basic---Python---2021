destination = input()

while destination != 'End':
    min_budget = float (input ())
    savings = 0

    while savings < min_budget:
        # Earning money till Ani has enough savings to start the trip
        curr_money_earned = float (input ())
        savings += curr_money_earned
    # Ani has enough savings in order to start the trip
    print(f'Going to {destination}!')

    destination = input()

# or


# available_sum = 0

# while True:
#     destination = input()
#     if destination == "End":
#         break
#     needed_money = float(input())

#     while available_sum < needed_money:
#         current_sum = float(input())
#         available_sum += current_sum

#     print(f"Going to {destination}!")
#     available_sum = 0














