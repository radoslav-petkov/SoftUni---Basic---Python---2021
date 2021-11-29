number_of_campaign_days = int(input())
number_of_bakers = int(input())
cakes_quantity = int(input())
waffles_quantity = int(input())
pancakes_quantity = int(input())

net_profit_for_one_bakers = (cakes_quantity * 45) + (waffles_quantity * 5.80) + (pancakes_quantity * 3.20)
total_profit_for_all_bakers_per_day = net_profit_for_one_bakers * number_of_bakers
profit_for_all_campaign = total_profit_for_all_bakers_per_day * number_of_campaign_days
total_sum = profit_for_all_campaign - (profit_for_all_campaign / 8)
print(total_sum)









