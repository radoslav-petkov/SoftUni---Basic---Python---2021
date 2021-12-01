wanted_book = input()
books_counter = 0

while True:
    current_name_of_book = input()

    if current_name_of_book == "No More Books":
        print('The book you search is not here!')
        print(f'You checked {books_counter} books.')
        break
    elif current_name_of_book == wanted_book:
        print(f"You checked {books_counter} books and found it.")
        break

    books_counter += 1


# or


# favourite_book = input()
#
# books_count = 0
# found_it = False
# book = input()
#
# while book != 'No More Books':
#     if book == favourite_book:
#         found_it = True
#         break
#     books_count += 1
#     book = input()
#
# if found_it:
#     print(f"You checked {books_count} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {books_count} books.")

#
# or
#
#
# searched_book = input()
#
# books_count = 0
#
# current_book = input()
#
# while current_book != searched_book:
#     if current_book == 'No More Books':
#         break
#
#     books_count += 1
#     current_book = input()
#
# if current_book == 'No More Books':
#     print('The book you search is not here!')
#     print(f'You checked {books_count} books.')
# else:
#     print(f'You checked {books_count} books and found it.')
#

# or
#
#
# book_name = input()
#
# book_count = 0
#
# is_book_found = False
#
# current_book = input()
# while current_book != 'No More Books':
#     if current_book == book_name:
#         is_book_found = True
#         print(f'You checked {book_count} books and found it.')
#         break
#
#     book_count += 1
#     current_book = input()
#
# if not is_book_found:
#     print('The book you search is not here!')
#     print(f'You checked {book_count} books.')



