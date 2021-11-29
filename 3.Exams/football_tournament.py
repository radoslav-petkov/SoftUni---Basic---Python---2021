club_name = input()
games_cnt = int(input())

total_points = 0
total_wins = 0
total_draws = 0
total_losts = 0

for i in range(games_cnt):
    curr_name_result = input()

    if curr_name_result == 'W':
        total_points += 3
        total_wins += 1
    elif curr_name_result == 'D':
        total_points += 1
        total_draws += 1
    elif curr_name_result == 'L':
        total_losts += 1

if games_cnt == 0:
    print(f'{club_name} hasn\'t played any games during this season.')
else:
    win_rate = (total_wins / games_cnt) * 100

    print(f'{club_name} has won {total_points} points during this season.')
    print('Total stats:')
    print(f'## W: {total_wins}')
    print(f'## D: {total_draws}')
    print(f'## L: {total_losts}')
    print(f'Win rate: {win_rate:.2f}%')





















