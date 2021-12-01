w = int(input())
l = int(input())

cake_peaces = w * l

while True:
    peace = input()
    if peace == 'STOP':
        print(f"{cake_peaces} pieces are left.")
        break

    cake_peaces -= int(peace)

    if cake_peaces <= 0:
        print(f"No more cake left! You need {abs(cake_peaces)} pieces more.")
        break


# or
#
# width = int(input())
# length = int(input())
# cake_size = width * length
#
# while cake_size > 0:
#     current_pieces_from_cake = input()
#
#     if current_pieces_from_cake == "STOP":
#         break
#
#     cake_size -= int(current_pieces_from_cake)
#
# if cake_size > 0:
#     print(f"{cake_size} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(cake_size)} pieces more.")
#
#
#














