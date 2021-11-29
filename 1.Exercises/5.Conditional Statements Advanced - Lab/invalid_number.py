number = int(input())

validator = 100 <= number <= 200 or number == 0
if not validator:
    print("invalid")


