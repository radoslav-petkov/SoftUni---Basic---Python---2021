import math

word = input()
list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'O', 'Y', 'I']

sum = 0
max_sum = 0
powerful_word = ''

while word != 'End of words':

#while not word == 'End of words':

    for letter in word:
        sum += ord(letter)

    if word[0] in list_of_vowels:
        sum = sum * len(word)
    elif word[0] not in  list_of_vowels:
        sum = math.floor(sum / len(word))

    if sum > max_sum:
        #max_sum = max(sum, max_sum)
        max_sum = sum
        powerful_word = word

    sum = 0
    word = input()

if word == 'End of words':

    print(f'The most powerful word is {powerful_word} - {max_sum}')

