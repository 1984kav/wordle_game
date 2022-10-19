def yellows_dict(test, word):
    yellows = {}

    for letter in set(test):
        if test.count(letter) <= word.count(letter):
            yellows[letter] = test.count(letter)
        else:
            yellows[letter] = word.count(letter)

    for letter_pos in range(len(test)):
        if test[letter_pos] == word[letter_pos]:
            yellows[test[letter_pos]] -= 1

    return yellows


print(yellows_dict(test='aaabbb',
                   word='bbbaac'))
