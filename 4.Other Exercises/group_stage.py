team_name = input()
games = int(input())
score = 0

all_goals = 0
all_goals_received = 0

for game in range(0, games):
    goals = int(input())
    goals_received = int(input())

    all_goals += goals
    all_goals_received += goals_received

    if goals > goals_received:
        score += 3
    elif goals == goals_received:
        score += 1

diff = all_goals-all_goal_recieved

if all_goals >= all_goal_recieved:
    print(f"{team_name} has finished the group phase with (score) points.")
    print(f"Goal difference: {diff}.")
else:
    print(f"{team_name} has been eliminated from the group phase.")
    print(f"Goal difference: {diff}.")