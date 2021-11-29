minutes_control = int(input ())
seconds_control = int(input())
length = float(input ())
seconds_per_100_reters = int(input ())

slope_time = (length / 100) * seconds_per_100_reters
additional_time = (length / 120) * 2.5
total_time = slope_time - additional_time
control_time = minutes_control * 60 + seconds_control

if total_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print (f"His time is {total_time:.3f}.")
else:
    need_seconds = total_time - control_time
    print(f"No, Marin failed! He was {need_seconds:.3f} second slower.")