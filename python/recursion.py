__author__ = 'daro'


def fibonacci(n):
    """

    :param n: dowolna liczba calkowita nieujemna
    :return: n-ta wartosc ciagu fibonacciego
    """
    assert type(n) == int and n >= 0, "zla wartosc n"
    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    assert type(n) == int and n >= 0, "zla wartosc n"
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


def palindrome(s):
    """

    :param s: dowolny ciag znakow
    :return: funkcja zwraca True jezeli ciag jest palindromem i False w przeciwnym razie
    """
    def correctString(s):
        s = s.replace(" ", "")
        s = s.lower()
        return s

    def isPal(s):
        if len(s) == 1 or len(s) == 0:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(correctString(s))
