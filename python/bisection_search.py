__author__ = 'daro'
from math import log


def find_root(x, power, epsilon = 0.0001):
    """
    Pierwiastek z x metoda binarna
    Input:
    :param x: float, Liczba z ktorej szukamy pierwiastek
    :param power: int, Potega liczby, power >= 0
    :param epsilon: Dokladnosc wyniku, epsilon > 0 dla float i epsilon >= 0 dla int
    :return: Pierwiastek potegi power z x zaokraglony do 4 miejsc po przecinku
    """
    try:
        x = float(x)
        power = int(power)
        epsilon = float(epsilon)
    except ValueError:
        print('Podano zla wartosc zmiennej do funkcji')
    if power == 0:
        return 1
    if power % 2 == 0 and x < 0 and power != 0:
        print('Podana zla wartosc')
        exit(1)

    low = min(-1, x)
    high = max(1, x)
    ans = (low + high) / 2.0
    while abs(ans**power - x) > epsilon:
        if ans**power > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2
    return round(ans, 4)


def bisection_search_game(low = 0, high = 100):
    """
    Gra
    Input (opcjonalnie):
    :param low: minimalna wartosc przedzialu poszukiwac
    :param high: maksymalna wartosc przedzialu poszukiwan - 1
    """
    try:
        low = int(min(low, high))
        high = int(max(low, high))
    except ValueError:
         print('Podano zla wartosc zmiennej do funkcji')

    tries = int(log(high - low, 2)) + 1
    print('Pomysl liczbe z przedzialu <%d, %d>. Mam %d prob na trafienie.' % (low, high-1, tries))
    while tries > 0:
        guess = (low + high) / 2
        print('\nPozostalo %d strzalow. Czy Twoja liczba to %s' % (tries, guess))
        ans = raw_input("Wprowadz 'l' jesli za mala, 'h' jesli za duza lub 'c' jesli zgadlem:  ")
        if ans == 'l':
            low = guess
            tries -= 1
        elif ans == 'h':
            high = guess
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
power = raw_input('Wprowadz potege: ')
print('Pierwiastek z ' + str(number) + ' to ' + str(find_root(number, power)))
