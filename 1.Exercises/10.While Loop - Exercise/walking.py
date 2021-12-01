goal = 10000

steps_count = 0

while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_count += steps

        if steps_count >= goal:
            print ("Goal reached! Good job!")
            print(f"{steps_count - goal} steps over the goal!")
        else:
            print(f"{goal - steps_count} more steps to reach goal.")
        break

    steps_count += int(steps)

    if steps_count >= goal:
        print("Goal reached! Good job!")
        print(f"{steps_count - goal} steps over the goal!")
        break


# command = input()
#
# total_steps_count = 0
#
# while command != "Going home":
#         steps_count = int(command)
#
#         total_steps_count += steps_count
#
#         if total_steps_count >= 10000:
#         # Goal reached
#             break
#
#         command = input()
#
# if command == "Going home":
#     home_steps = int(input())
#     total_steps_count += home_steps
#
# if total_steps_count >= 10000:
#     print("Goal reached! Good job!")
#     print(f"{total_steps_count - 10000} steps over the goal!")
# else:
#     print(f"{10000 - total_steps_count} more steps to reach goal.")



 # or



#
# target_steps = 10000
# current_steps = 0
# going_home = False
#
# while current_steps < target_steps:
#     command = input()
#     if command == "Going home":
#         going_home = True
#         break
#
#     steps = int(command)
#     current_steps += steps
#
# difference = abs (current_steps - target_steps)
#
# if current_steps >= target_steps:
#     print("Goal reached! Good job!")
#     print(f"{difference} steps over the goal!")
# else:
#     print(f"{difference} more steps to reach goal.")


