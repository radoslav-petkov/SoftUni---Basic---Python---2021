judges_count = int(input())
presentation_name = input ()

average_score_sum = 0
presentations_count = 0

while presentation_name != 'Finish':
    average_score = 0
    for _ in range(judges_count):
        average_score += float(input())
    average_score /= judges_count
    print(f"{presentation_name} - {average_score:.2f}.")

    average_score_sum += average_score
    presentations_count += 1
    presentation_name = input()

average_score_sum /= presentations_count
print (f"Student's final assessment is {average_score_sum: .2f}.")


# or
#
#
# number_of_people_on_the_jury = int(input())
# all_grades = 0
# current_grades = 0
# counter = 0
#
# while True:
#     name_of_presentation = input()
#     if name_of_presentation == "Finish":
#         print(f"Student's final assessment is {all_grades / counter:.2f}.")
#         break
#
#     for x in range(number_of_people_on_the_jury):
#         grade = float(input())
#         current_grades += grade
#         all_grades += grade
#         counter += 1
#
#     print(f"{name_of_presentation} - {current_grades / number_of_people_on_the_jury:.2f}.")
#     current_grades = 0
















