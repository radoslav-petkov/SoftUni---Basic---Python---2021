rest_days = int(input())

game_norm = 30000
game_minutes = rest_days * 127
work_days = (365 - rest_days) * 63

time_for_play = work_days + game_minutes

time_left = abs(game_norm - time_for_play)  #!!!!!!!!!!!!!!!!!!!!!!!!!
hours = time_left // 60
minutes = time_left % 60

if game_norm >= time_for_play:

    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")