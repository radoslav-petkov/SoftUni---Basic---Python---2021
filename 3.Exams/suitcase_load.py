airplane_capacity = float(input())
counter = 0

while True:
    suitcase = input()

    if suitcase == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        suitcase = float(suitcase)

    # if suitcase > airplane_capacity:
    #     print("No more space!")
    #     break

    if (counter + 1) % 3 == 0:

        suitcase *= 1.1

    if suitcase > airplane_capacity:
        print("No more space!")
        break

    counter += 1
    airplane_capacity -= suitcase

print(f'Statistic: {counter} suitcases loaded.')


# or
#
# boot_capacity = float(input())
# suitcase_volume = input()
# total_volume = 0
# suitcases_counter = 1
#
# while suitcase_volume != "End":
#     suitcase_volume = input()
#     if suitcases_counter % 3 == 0:
#         total_volume = total_volume + (float(suitcase_volume) * 0.1)
#         suitcases_counter += 1
#     else:
#         suitcases_counter += 1
#         total_volume += float(suitcase_volume)
#
# if boot_capacity < total_volume:
#     print("No more space!")
#     print(f"Statistic: {suitcases_counter} suitcases loaded.")
# else:
#     print("Congratulations! All suitcases are loaded!")
#     print(f"Statistic: {suitcases_counter} suitcases loaded.")