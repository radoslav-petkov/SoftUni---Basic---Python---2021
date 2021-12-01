failed_threshhold = int(input())

bad_grades_counter = 0
name_of_last_problem = " "
problems_counter = 0
grades_sum = 0

while True:
    name_of_problem = input()
    if name_of_problem == "Enough":
        break

    grade = int(input())

    if grade <= 4:
        bad_grades_counter += 1

        if bad_grades_counter >= failed_threshhold:
            break

    name_of_last_problem = name_of_problem
    problems_counter += 1
    grades_sum += grade

if bad_grades_counter < failed_threshhold:
    average_score = grades_sum / problems_counter
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems_counter}")
    print(f"Last problem: {name_of_last_problem}")

else:
    print(f"You need a break, {bad_grades_counter} poor grades.")

# or
#
# count_bad_grades = int(input())
# current_count_bad_grades = 0
#
# total_grades = 0
# count_grades = 0
#
# line = input()
# while line != "Enough":
#     task_name = line
#     grade = int(input())
#     count_grades += 1
#     total_grades += grade
#
#     if grade <= 4:
#         current_count_bad_grades += 1
#
#     if current_count_bad_grades == count_bad_grades:
#         print(f'You need a break, {count_bad_grades} poor grades.')
#         break
#
#     line = input()
#
# if line == 'Enough':
#     average_grades = total_grades / count_grades
#     print(f"Average score: {average_grades:.2f}")
#     print(f"Number of problems: {count_grades}")
#     print(f"Last problem: {task_name}")

