import math

record = float(input ())
meters = float(input())
seconds_per_meter = float(input ())
total_seconds = meters * seconds_per_meter
# We slow down with 30 seconds every 50th meter
slow_downs_cnt = math.floor (meters / 50)
total_seconds += slow_downs_cnt * 30
if total_seconds < record:
    # Record is beaten
    print(f"Yes! The new record is {total_seconds:.2f} seconds.")
else:
    # Record is not beaten
    add_seconds = total_seconds - record
    print(f"No! He was {add_seconds:.2f} seconds slower.")















