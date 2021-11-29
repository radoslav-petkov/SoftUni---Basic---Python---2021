from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_swimming_one_meter = float(input())

total_time_in_seconds = distance_in_meters * time_in_seconds_for_swimming_one_meter
additional_time = floor(distance_in_meters / 15) * 12.5
total_time = total_time_in_seconds + additional_time

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff_time = total_time - record_in_seconds
    print(f"No, he failed! He was {diff_time:.2f} seconds slower.")
