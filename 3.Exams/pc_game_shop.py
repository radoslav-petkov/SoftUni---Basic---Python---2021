n = int(input())

hearthstone_cnt = 0
fornite_cnt = 0
overwatch_cnt = 0
other_cnt = 0

for i in range(n):
 current_game = input()

 if current_game == "Hearthstone":
     hearthstone_cnt += 1
 elif current_game == "Fornite":
     fornite_cnt += 1
 elif current_game == "Overwatch":
     overwatch_cnt += 1
 else:
     other_cnt += 1

hearthstone_percent = hearthstone_cnt / n * 100
print(f"Hearthstone - {hearthstone_percent:.2f}%")

fornite_percent = fornite_cnt / n * 100
print(f"Fornite - {fornite_percent:.2f}%")

overwatch_percent = overwatch_cnt / n * 100
print(f"Overwatch - {overwatch_percent:.2f}%")

other_games_percent = other_cnt / n * 100
print(f"Others - {other_games_percent:.2f}%")



















