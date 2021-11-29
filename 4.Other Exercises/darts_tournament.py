start_points = int(input())
points = start_points
moves_counter = 0
has_won_bullseye = False
has_lost = False

while points > 0:
    move_type = input()
    moves_counter += 1
    # 2.3. Check if bullseye
    if move_type == 'bullseye':
        has_won_bullseye = True
        break

    current_points = int(input())

    if move_type == 'double ring':
        current_points *= 2
    elif move_type == 'triple ring':
        current_points *= 3

    points -= current_points

    if points < 0:
        has_lost = True

has_won = points == 0

if has_won:
    print(f'Congratulations! You won the game in {moves_counter} moves!')
elif has_won_bullseye:
    print(f'Congratulations! You won the game with a bullseye in {moves_counter} moves!')
elif has_lost:
    print(f'Sorry, you lost. Score difference: {abs(points)}.')
                                     I