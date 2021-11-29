passengers = int(input())
stops = int(input())

for i in range(1, stops + 1):
    if bus_stop_count % 2 == 0:
        passenger_count -= (passenger_depart + 2)
        passenger_count += passenger_arival
    else:
        passenger_count -= passenger_depart
        passenger_count += (passenger_arival + 2)

print(f"The final number of passengers is : {passengers}")

# or
#
# passengers = int(input())
# stops = int(input())
#
# for i in range(1, stops + 1):
#     passengers -= int(input())
#     passengers += int(input())
#
#     passengers += 2 if i % 2 != 0 else -2
#
# print(f"The final number of passengers is : {passengers}")