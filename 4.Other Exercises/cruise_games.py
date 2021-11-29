from math import floor

player_name = input()
games_count = int(input())

volleyball_points = 0
tennis_points = 0
badminton_points = 0
volleyball_count = 0
tennis_count = 0
badminton_count = 0

for i in range(games_count):
    game_name = input()
    points = int(input())
    if game_name == "volleyball":
        volleyball_points += points * 1.07
        volleyball_count += 1
    elif game_name == "tennis":
        tennis_points += points * 1.05
        tennis_count += 1
    elif game_name == "badminton":
        badminton_points += points * 1.02
        badminton_count += 1

volleyball_average = floor(volleyball_points / volleyball_count)
tennis_average = floor(tennis_points / tennis_count)
badminton_average = floor(badminton_points / badminton_count)
total_points = floor(volleyball_points + tennis_points + badminton_points)

if volleyball_average >= 75 and tennis_average >= 75 and badminton_average >= 75:
    print(f"Congratulations, {player_name}! You won the cruise games with {total_points} points.")
else:
    print(f"Sorry, {player_name}, you lost. Your points are only {total_points}.")

    # or
    #
    # from math import floor as fl
    #
    # name = input()
    # games = int(input())
    # volleyball_games = 0
    # tennis_games = 0
    # badminton_games = 0
    # volleyball_score = 0
    # tennis_score = 0
    # badminton_score = 0
    #
    # for g in range(games):
    #     game = input()
    #     points = int(input())
    #
    #     if game == "volleyball":
    #         volleyball_games += 1
    #         volleyball_score += points * 1.07
    #     elif game == "tennis":
    #         tennis_games += 1
    #         tennis_score += points * 1.05
    #     elif game == "badminton":
    #         badminton_games += 1
    #         badminton_score += points * 1.02
    # score = volleyball_score + tennis_score + badminton_score
    #
    # if volleyball_score / volleyball_games >= 75 and tennis_score / tennis_games >= 75 and badminton_score / badminton_games >= 75:
    #     print(f"Congratulations, {name}! You won the cruise games with {fl(score)} points.")
    # else:
    #     print(f"Sorry, {name}, you lost. Your points are only {fl(score)}.")








