deposit_sum = float(input())
term_in_months = int(input())
yearly_dividend_percent = float(input())

dividend = deposit_sum * yearly_dividend_percent / 100
dividend_for_one_month = dividend / 12
total_sum = deposit_sum + (term_in_months * dividend_for_one_month)
print(total_sum)








