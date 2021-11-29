bitcoins_cnt = int(input())
chinese_van = float(input())
commission_percent = float (input())

bitcoins_to_bgn = bitcoins_cnt * 1168
chinese_van_to_usd = chinese_van * 0.15
usd_to_bgn = chinese_van_to_usd * 1.76

total_sum_bgn = bitcoins_to_bgn + usd_to_bgn

total_euro = total_sum_bgn / 1.95
commission_value = (commission_percent / 100) * total_euro
# Here we subtract commission value from the totol sum
total_euro -= commission_value
print(f'{total_euro:.2f}')


















