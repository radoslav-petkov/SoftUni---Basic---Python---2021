type_of_year = input()
number_of_holidays = int(input())
number_of_weekends = int(input())

number_of_games = ((48 - number_of_weekends) * 3/4) + number_of_weekends + (number_of_holidays * 2/3)
if type_of_year == "leap":
    number_of_games += number_of_games * 0.15

print(int(number_of_games))