from math import ceil
series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
break_time = break_duration * 1/4

time_left = break_duration - lunch_time - break_time

if episode_duration <= time_left:
    print(f"You have enough time to watch {series_name} and left with "
          f"{ceil(time_left - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need "
          f"{ceil(episode_duration - time_left)} more minutes.")

