from random import choice as random_choice
from words_5 import popular_words_5, all_words_5


def color_print(test_word, computer_word):
    def red_print(text):
        print('\033[1;31m', text.upper(), '\033[0m', sep='', end=' ')

    def green_print(text):
        print('\033[1;32m', text.upper(), '\033[0m', sep='', end=' ')

    def yellow_print(text):
        print('\033[1;33m', text.upper(), '\033[0m', sep='', end=' ')

    dict_letter_word = {letter: computer_word.count(letter) for letter in set(computer_word)}

    for letter_index in range(len(test_word)):
        if test_word[letter_index] == computer_word[letter_index]:
            green_print(test_word[letter_index])
            dict_letter_word[test_word[letter_index]] -= 1

        elif test_word[letter_index] in computer_word and dict_letter_word[test_word[letter_index]] > 0:
            yellow_print(test_word[letter_index])
            dict_letter_word[test_word[letter_index]] -= 1

        else:
            red_print(test_word[letter_index])
    print('\033[0m', sep='', end='\n')


word = random_choice(popular_words_5)
attempt = 0
print(f'Я загадал слово их {len(word)} букв...\n')

while True:
    attempt += 1
    test = input(f'Попытка № {attempt} Введите слово: ').lower()
    while test not in all_words_5:
        test = input('Нет такого слова. Введите слово: ').lower()
    color_print(test, word)
    if test == word:
        print('ПОБЕДА!!!')
        input('Для выхода нажмите ENTER...')
        break
