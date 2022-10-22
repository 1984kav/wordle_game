from random import choice as choice
from dictionaries import popular_words_5, other_words_5


def color_print(test_word, computer_word):
    def red_print(text):
        print('\033[1;31m', text.upper(), '\033[0m', sep='', end=' ')

    def green_print(text):
        print('\033[1;32m', text.upper(), '\033[0m', sep='', end=' ')

    def yellow_print(text):
        print('\033[1;33m', text.upper(), '\033[0m', sep='', end=' ')

    def yellows_dict(test_word, computer_word):
        yellows = {}

        for letter in set(test_word):
            if test_word.count(letter) <= computer_word.count(letter):
                yellows[letter] = test_word.count(letter)
            else:
                yellows[letter] = computer_word.count(letter)

        for letter_pos in range(len(test_word)):
            if test_word[letter_pos] == computer_word[letter_pos]:
                yellows[test_word[letter_pos]] -= 1

        return yellows

    dict_yellow = yellows_dict(test_word, computer_word)

    for letter_index in range(len(test_word)):
        if test_word[letter_index] == computer_word[letter_index]:
            green_print(test_word[letter_index])

        elif test_word[letter_index] in computer_word and dict_yellow[test_word[letter_index]] > 0:
            yellow_print(test_word[letter_index])
            dict_yellow[test_word[letter_index]] -= 1

        else:
            red_print(test_word[letter_index])
    print('\033[0m', sep='', end='\n')


word = choice(popular_words_5)
test_words = []
attempt = 0
print(f'Я загадал слово из {len(word)} букв...')

while True:
    attempt += 1
    test = input(f'\nПопытка № {attempt} Введите слово: ').lower()

    while len(test) != len(word) or (test not in popular_words_5 and test not in other_words_5):
        if len(test) != len(word):
            test = input(f'Длина слова не равна {len(word)}! Введите слово: ').lower()
            continue
        if test not in popular_words_5 and test not in other_words_5:
            test_word = input(f'Нет такого слова! Введите слово: ').lower()

    test_words.append(test)
    print('\n' * 100)
    for test in test_words:
        color_print(test, word)

    if test == word:
        print('ПОБЕДА!!!')
        input('Для выхода нажмите ENTER...')
        break
