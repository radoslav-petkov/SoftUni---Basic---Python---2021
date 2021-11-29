name_of_best_player = " "
number_of_goals_of_best_player = 0

while True:
    name_of_player = input()
    if name_of_player == "END":
        break

    number_of_goals = int(input())

    if number_of_goals > number_of_goals_of_best_player:
        name_of_best_player = name_of_player
        number_of_goals_of_best_player = number_of_goals

        if number_of_goals >= 10:
            break
print(f"{name_of_best_player} is the best player!")
if number_of_goals_of_best_player >= 3:
    print(f"He has scored {number_of_goals_of_best_player} goals and made a hat-trick !!!")
else:
    print(f"He has scored {number_of_goals_of_best_player} goals.")

