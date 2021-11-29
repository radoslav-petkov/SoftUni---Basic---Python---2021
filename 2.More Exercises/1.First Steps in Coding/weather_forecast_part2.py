# Step 1 Set input
weather_in_celsius = float(input())

# Step 2 Set weather intervals
if weather_in_celsius >= 26.00 and weather_in_celsius <= 35.00:
    print("Hot")
elif weather_in_celsius >= 20.1 and weather_in_celsius <= 25.9:
    print("Warm")
elif weather_in_celsius >= 15.00 and weather_in_celsius <= 20.00:
    print("Mild")
elif weather_in_celsius >= 12.00 and weather_in_celsius <= 14.9:
    print("Cool")
elif weather_in_celsius >= 5.00 and weather_in_celsius <= 11.9:
    print("Cold")
else:
    print("unknown")


