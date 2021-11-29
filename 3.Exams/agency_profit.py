airline  = input()
adults_ticket = int(input())
kids_ticket = int(input())
ticket_adult_cost_ = float(input())
service_cost = float(input())
net_sum = 0

ticket_kids_cost = ticket_adult_cost_ - (ticket_adult_cost_ * 0.70)
cost_ticket_adult_service = ticket_adult_cost_ + service_cost
cost_ticket_kids_service = ticket_kids_cost + service_cost
ticket_cost = (kids_ticket * cost_ticket_kids_service) + (adults_ticket * cost_ticket_adult_service)
net_sum = 0.20 * ticket_cost

print(f"The profit of your agency from {airline} tickets is {net_sum:.2f} lv.")


















