shooting_minutes = int(input())
scene_count = int(input())
timeline_scene = int(input())

preparation_time = 0.15 * shooting_minutes
time_for_shooting = scene_count * timeline_scene
needed_time = preparation_time + time_for_shooting

if shooting_minutes > needed_time:
    time_left = shooting_minutes - needed_time
    print(f"You managed to finish the movie on time! You have {round(time_left)} minutes left!")
else:
    time_needed = needed_time - shooting_minutes
    print(f"Time is up! To complete the movie you need {round(time_needed)} minutes.")



