results = [input().split(':') for result in range(3)]

wins = 0
loses = 0
draws = 0

for _ in range(len(results)):
    team_one_goals = int(results[0][0])
    team_two_goals = int(results[0][1])

    if team_one_goals > team_two_goals:
        wins += 1
    elif team_one_goals < team_two_goals:
        loses += 1
    else:
        draws += 1

    results.remove(results[0])

print(f'Team won {wins} games.')
print(f'Team lost {loses} games.')
print(f'Drawn games: {draws}')