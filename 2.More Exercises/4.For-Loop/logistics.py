cargo_count = int(input())

microbus_tonage = 0
truck_tonage = 0
train_tonage = 0
total_tonage = 0

for i in range(1, cargo_count + 1):
    tonage = int(input())
    if tonage <= 3:
        microbus_tonage += tonage
    if 4 <= tonage <= 11:
        truck_tonage += tonage
    if tonage >= 12:
        train_tonage += tonage

total_tonage = microbus_tonage + truck_tonage + train_tonage
average_tonage = (microbus_tonage * 200 + truck_tonage * 175 + train_tonage * 120)/total_tonage

microbus_tonage_percent = (microbus_tonage/total_tonage) * 100
truck_tonage_percent = (truck_tonage/total_tonage) * 100
train_tonage_percent = (train_tonage/total_tonage) * 100

print(f"{average_tonage:.2f}")
print(f"{microbus_tonage_percent:.2f}%")
print(f"{truck_tonage_percent:.2f}%")
print(f"{train_tonage_percent:.2f}%")

