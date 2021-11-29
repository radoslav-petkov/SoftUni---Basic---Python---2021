peoples = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
shake_count = 0
bar_count = 0

for p in range(1, peoples + 1):
   activity = input ()

   if activity == 'Back':
      back_count += 1
   elif activity == 'Chest':
      chest_count += 1
   elif activity == 'Legs':
      legs_count += 1
   elif activity == 'Abs':
      abs_count += 1
   elif activity == 'Protein shake':
      shake_count += 1
   elif activity == 'Protein bar':
      bar_count += 1

print(f' {back_count} - back')
print(f'{chest_count} - chest')
print(f'{legs_count} - legs')
print(f'{abs_count} - abs')
print(f'{shake_count} - protein shake')
print(f'{bar_count} - protein bar')
print(f'{(back_count + chest_count + legs_count + abs_count) / peoples * 100:.2f}% - work out')
print(f'{(shake_count + bar_count) / peoples * 100:.2f}% - protein')















