fans_bud_init = float(input())
cat = input()
fans_num = int(input())

sum_needed = 0
pure_bud = 0
ticket = 0

if cat == 'Normal':
    ticket = 249.99
elif cat == 'VIP':
    ticket = 499.99

if fans_num >= 1 and fans_num <= 4:
    pure_bud = fans_bud_init - ( ( fans_bud_init / 100 ) * 75 )
elif fans_num <=9:
    pure_bud = fans_bud_init - ( ( fans_bud_init / 100 ) * 60 )
elif fans_num >= 10 and fans_num <= 24:
    pure_bud = fans_bud_init - ( ( fans_bud_init / 100 ) * 50 )
elif fans_num >= 25 and fans_num <=49:
    pure_bud = fans_bud_init - ( ( fans_bud_init / 100 ) * 40 )
elif fans_num >= 50:
    pure_bud = fans_bud_init - ( ( fans_bud_init / 100 ) * 25 )


sum_needed = ticket * fans_num

sum_lack = sum_needed - pure_bud
sum_over = pure_bud - sum_needed

if sum_needed > pure_bud:
    print(f'Not enough money! You need {sum_lack:.2f} leva.')
elif sum_needed < pure_bud:
    print(f'Yes! You have {sum_over:.2f} leva left.')