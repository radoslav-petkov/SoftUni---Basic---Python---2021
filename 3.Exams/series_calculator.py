import math

series_nane = input()
count_seasons = int(input())
count_episodes = int(input())
watch_time_episode =  float(input())

total_time_episode = watch_time_episode + (0.2 * watch_time_episode)
additional_time = count_seasons * 10

total_time_series = (count_seasons * count_episodes * total_time_episode) + additional_time

print(f"Total time needed to watch the {series_nane} series is {math.floor(total_time_series)} minutes.")
