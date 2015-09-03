__author__ = 'daro'
from math import log


def find_root(x):
    """
    Pierwiastek z x metoda binarna
    Input:
    :param x: Dowolna liczba nieujemna
    :return: Pierwiastek z x zaokraglony do 4 miejsc po przecinku z bledem epsilon
    """
    try:
        x = float(x)
    except ValueError:
        print('Podano zla wartosc zmiennej do funkcji')
    if x < 0:
        print('Podana zla wartosc')
        exit(1)

    min = 0
    max = x
    epsilon = 0.0001
    ans = (min + max) / 2
    while abs(ans**2 - x) > epsilon:
        if ans**2 > x:
            max = ans
        else:
            min = ans
        ans = (min + max) / 2
    return round(ans, 4)


def bisection_search_game(min = 0, max = 100):
    """
    Gra
    Input (opcjonalnie):
    :param min: minimalna wartosc przedzialu poszukiwac
    :param max: maksymalna wartosc przedzialu poszukiwan - 1
    """
    try:
        min = int(min)
        max = int(max)
    except ValueError:
         print('Podano zla wartosc zmiennej do funkcji')
    if min > max:
        print('Wartosc minimalna nie moze byc wieksza od maksymalnej')
        exit(1)

    tries = int(log(max - min, 2)) + 1
    print('Pomysl liczbe z przedzialu <%d, %d>. Mam %d prob na trafienie.' % (min, max-1, tries))
    while tries > 0:
        guess = (min + max) / 2
        print('\nPozostalo %d strzalow. Czy Twoja liczba to %s' % (tries, guess))
        ans = raw_input("Wprowadz 'l' jesli za mala, 'h' jesli za duza lub 'c' jesli zgadlem:  ")
        if ans == 'l':
            min = guess
            tries -= 1
        elif ans == 'h':
            max = guess
            tries -= 1
        elif ans == 'c':
            print('Koniec gry. Twoja liczba to %d' % guess)
            break
        else:
            print('Podano zla odpowiedz')
    else:
        print('\nOszukiwales')


bisection_search_game()
number = raw_input('Wprowadz liczbe: ')
print('Pierwiastek z ' + str(number) + ' to ' + str(find_root(number)))
