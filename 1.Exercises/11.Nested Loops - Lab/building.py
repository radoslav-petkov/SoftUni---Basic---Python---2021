floors_count = int(input())
rooms_count = int(input ())

for floor_num in range (floors_count, 0, -1):
    for room_num in range (0, rooms_count):
        if floor_num == floors_count:
            # I am on the last floor and here we have large apartments 'L'
            print(f'L{floor_num}{room_num}', end=' ')
        elif floor_num % 2 == 0:
           # I am on even floor and here we have offices '0'
            print(f'0{floor_num}{room_num}', end=' ')
        else:
            # I am on odd floor and here we have standart apartments 'A'
            print(f'A{floor_num}{room_num}', end=' ')
    # Move to the next floor
    print('')


# or

# number_of_floors = int(input())
# number_of_rooms = int(input())


# for x in range(number_of_floors, 0, -1):
#     current_floor = x * 10
#     for a in range(number_of_rooms):
#         current_number_of_room = current_floor + a
#         if x == number_of_floors:
#             print(f"L{current_number_of_room}", end =" ")
#         elif x % 2 != 0:
#             print(f"A{current_number_of_room}", end = " ")
#         else:
#             print(f"O{current_number_of_room}", end=" ")

#     print()















