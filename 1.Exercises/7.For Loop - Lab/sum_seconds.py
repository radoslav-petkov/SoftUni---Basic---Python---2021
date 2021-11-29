first_name = int(input())
second_name = int(input())
third_name = int(input())
total_time = first_name + second_name + third_name
minutes = total_time // 60
seconds = total_time % 60

if seconds <=10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")























