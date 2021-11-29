capacity = int(input())

total_people = 0

space_left = capacity  # това не трябва да е 0.

final_price = 0

# command = input() - това трябва да е в цикъла.

while True:  # while command!="Movie time!": цикъла може да изглежда така.

    command = input()

    if command == "Movie time!":  # тази проверка я вкарваме в цикъла.

        space_left = space_left - total_people

        print(f"There are {space_left} seats left in the cinema.")

        break  # ако влезем в този if трябва да приключи цикъла.

    people = int(command)

    price = people * 5

    if people % 3 == 0:
        price -= 5  # отстъпката е 5 лева, а не 5%.

    # if total_people>capacity: това не отговаря на условието.

    if people > capacity:  # (Ако в залата се опитат да влязат повече хора от колкото места са останали) според условието.

        print("The cinema is full.")

        break

    final_price += price

    total_people += people

    capacity -= people  # намаляме местата с броя на хората които влизат.

# command = input() - това е излишно


print(f'Cinema income - {final_price} lv.')


