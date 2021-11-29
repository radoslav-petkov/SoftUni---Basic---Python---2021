target_height = int(input())
current_height = target_height - 30

total_jumps = 0
failed = False
counter_failed = 0

while not failed:
    jump = int(input())
    total_jumps = total_jumps + 1

    if jump <= current_height:
        counter_failed = counter_failed + 1
        if counter_failed == 3:
            failed = True
    else:
        if current_height >= target_height:
            break
        current_height = current_height + 5
        counter_failed = 0

if not failed:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")