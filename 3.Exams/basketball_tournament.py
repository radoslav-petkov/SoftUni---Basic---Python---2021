won_matches = 0
lost_matches = 0
total_matches = 0
command = input ()

while command != "End of tournaments":
    current_tournir_name = command
    number_of_games = int(input())

    for current_game in range (1, number_of_games + 1):
        total_matches += 1
        desi_team_points = int (input ())
        other_team_points = int(input ())
        difference = abs(desi_team_points - other_team_points)

        if desi_team_points > other_team_points:
            won_matches += 1
            print(f"Game {current_game} of tournament {current_tournir_name}: win with {difference} points.")
        else:
            lost_matches += 1
            print(f"Game {current_game} of tournament {current_tournir_name}: lost with {difference} points.")
    command = input ()
won_matches_percent = won_matches / total_matches * 100
lost_matches_percent = lost_matches / total_matches * 100
print(f"{won_matches_percent:.2f}% matches win")
print(f"{lost_matches_percent:.2f}% matches lost")