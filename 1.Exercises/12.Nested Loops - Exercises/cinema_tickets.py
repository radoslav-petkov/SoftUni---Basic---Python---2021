movie_name = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != 'Finish':
   free_seats = int (input())
   seats_taken = 0

   ticket_type = input()
   while ticket_type != 'End':
       if ticket_type == 'student':
           student_tickets += 1
       elif ticket_type == 'standard':
           standard_tickets + 1
       elif ticket_type == 'kid':
           kid_tickets += 1
       seats_taken += 1
       if free_seats - seats_taken == 0:
           break

       ticket_type = input()

   print(f"{movie_name} {seats_taken / free_seats * 100:.2f}% full.")
   movie_name = input()

all_tickets = standard_tickets + student_tickets + kid_tickets
print(f"Total tickets: {all_tickets}")
print(f"{student_tickets / all_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / all_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / all_tickets * 100:.2f}% kids tickets. ")


# or
#
#
#
# number_of_tickets = 0
# counter = 0
# standard = 0
# current_standard = 0
# kid = 0
# current_kid = 0
# student = 0
# current_student = 0
#
# while True:
#     name_of_movie = input()
#
#     if name_of_movie == "Finish":
#         break
#
#     number_of_seats = int(input())
#
#     while True:
#         type_of_ticket = input()
#
#         if type_of_ticket == "End":
#             break
#
#         counter += 1
#         number_of_tickets += 1
#
#         if type_of_ticket == "standard":
#             standard += 1
#             current_standard += 1
#
#         elif type_of_ticket == "kid":
#             kid += 1
#             current_kid += 1
#
#         elif type_of_ticket == "student":
#             student += 1
#             current_student += 1
#
#         if counter >= number_of_seats:
#             break
#
#     print(f"{name_of_movie} - {(counter / number_of_seats) * 100:.2f}% full.")
#     current_student = 0
#     current_kid = 0
#     current_standard = 0
#     counter = 0
#
#
# print(f"Total tickets: {number_of_tickets}")
# print(f"{(student / number_of_tickets) * 100:.2f}% student tickets.")
# print(f"{(standard / number_of_tickets) * 100:.2f}% standard tickets.")
# print(f"{(kid / number_of_tickets) * 100:.2f}% kids tickets.")














