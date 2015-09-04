__author__ = 'daro'


def vowel_counter(s):
    vowel = 0
    for char in s:
        if char in 'aeiouy':
            vowel += 1
    return vowel


def substring_counter(s, sub):
    """

    :param s: Dowolny ciag znakow
    :param sub: dowolny ciag znakow
    :return: Funkcja wypisuje ilosc wystapien ciagu sub w ciagu s
    """
    number = 0
    index = 0
    while True:
        index = s.find(sub, index)
        if index == -1:
            break
        else:
            number += 1
            index += 1
    print('Number of times %s occurs is: %d' % (sub, number))


def alphabetical_substring(s):
    """

    :param s: dowolny ciag znakow
    :return: funkcja wypisuje najdluzszy podciag znakow ulozonych alfabetycznie
    """
    flag = True
    substring = ''
    for char in s:
        if flag:
            flag = False
            last = char
            temp_substring = char
            continue
        if last <= char:
            temp_substring += char
        else:
            if len(substring) < len(temp_substring):
                substring = temp_substring
            temp_substring = char
        last = char
    else:
        if len(substring) < len(temp_substring):
                substring = temp_substring
    print('Longest substring in alphabetical order is: %s' % substring)

