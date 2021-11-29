voucher_value = int(input())
movie_price = 0
product_price = 0
movie_counter = 0
product_counter = 0

while True:
    command = input()

    if command == "End":
        break

    if len(command) > 8:
        movie_price += ord(command[0]) + ord(command[1])

        if voucher_value < movie_price:
            break
        voucher_value -= movie_price
        movie_counter += 1
        movie_price = 0

    else:
        product_price += ord(command[0])

        if voucher_value < product_price:
            break

        voucher_value -= product_price
        product_counter += 1
        product_price = 0

print(movie_counter)
print(product_counter)
