movie_name = input()
count_days = int(input ())
count_tickets = int(input())
price_ticket = float(input ())
percent = int(input())

sum_tickets_per_day = count_tickets * price_ticket
sum_tickets_all_days = sum_tickets_per_day * count_days
sum_for_cinema = percent / 100 * sum_tickets_all_days
profit = sum_tickets_all_days - sum_for_cinema

print (f"The profit from the movie {movie_name} is {profit:.2f} lv.")