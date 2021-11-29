total_steps_count = 0

command = input()

while command != "Going home":
        steps_count = int(command)

        total_steps_count += steps_count

        if total_steps_count >= 10000:
        # Goal reached
            break

        command = input()

if command == "Going home":
    home_steps = int(input())
    total_steps_count += home_steps

if total_steps_count >= 10000:
    print("Goal reached! Good job!")
    print(f"{total_steps_count - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps_count} more steps to reach goal.")