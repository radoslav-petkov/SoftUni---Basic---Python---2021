command = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0
while command != 'stop':
    is_prime = True
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        continue
    else:
    #(2 -> current_number) % current_number == 0
    for number in range (2, current_number):
        if current_number % number == 0:
            is_prime = False
    if is_prime:
        prime_numbers_sum += current_number
    else:
        non_prime_numbers_sum += current_number
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
#
#
#
#or
#
#
# sum_of_prime_numbers = 0
# sum_of_non_prime_numbers = 0
# command = input()
#
# while command != "stop":
#     current_number = int(command)
#     if current_number < 0:
#         print("Number is negative.")
#         command = input()
#         continue
#
#     number_is_prime = True
#     for number in range(2, current_number):
#         if current_number % number == 0:
#             number_is_prime = False
#             break
#
#     if number_is_prime:
#         sum_of_prime_numbers += current_number
#     else:
#         sum_of_non_prime_numbers += current_number
#     command = input()
#
# print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
# print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
#
#
#







