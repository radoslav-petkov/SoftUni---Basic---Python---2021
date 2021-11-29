from math import floor
necesassy_hours = float(input())
available_days = float(input())
overtime_workers_count = float(input())

trainig_time = available_days - (available_days * 0.1)
working_hours = trainig_time * 8
overtime_hours = overtime_workers_count * (2 * available_days)
total_hours = floor(working_hours + overtime_hours)

if total_hours >= necesassy_hours:
    hours_left = floor(total_hours - necesassy_hours)
    print(f"Yes!{hours_left:.0f} hours left.")
else:
    needed_hours = floor(necesassy_hours - total_hours)
    print(f"Not enough time!{needed_hours:.0f} hours needed.")