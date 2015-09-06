__author__ = 'daro'


def minimum_debt_pay_calculation(balance, annualInterestRate, monthlyPaymentRate, monthMax):
    """

    :param balance: (int lub float) Kwota kredytu do splacenia
    :param annualInterestRate: (int lub float) stopa procentowa odsetek w skali roku
    :param monthlyPaymentRate: (int lub float)stopa procentowa miesiecznej minimalnej kwoty do splacenia
    :param monthMax: (int) okres przez jaki ma byc stworzona kalkulacja
    :return Program pokazuje kalkulacje splaty kredytu przez okreslony okres przy placeniu minimalnej miesiecznej raty
    """
    monthlyPaymentRate = float(monthlyPaymentRate)
    monthlyInterestRate = annualInterestRate / 12.0
    previousBalance = balance
    month = 0
    totalPaid = 0
    while month < monthMax:
        minimumMonthlyPayment = monthlyPaymentRate * previousBalance
        monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
        totalPaid += minimumMonthlyPayment
        previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        print('Month: %d' % (month + 1))
        print('Minimum monthly payment: %.2f' % minimumMonthlyPayment)
        print('Remaining balance: %.2f' % previousBalance)
        month += 1
    print('Total paid: %.2f' % totalPaid)
    print('Remaining balance: %.2f' % previousBalance)


def debt_payoff_year_calculation(balance, annualInterestRate):
    """

    :param balance: (int lub float) kwota kredytu do splacenia
    :param annualInterestRate: (int lub float) stopa procentowa odsetek w skali roku
    :return: Program wylicza kwote miesiecznej raty w celu splacenia calego kredytu w ciagu 1 roku \
    orzy czym miesieczna rata jest wielokrotnoscia kwoty 10
    """
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayment = 10
    while True:
        month = 0
        preview_balance = balance
        while month < 12:
            monthlyUnpaidBalance = preview_balance - monthlyPayment
            preview_balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
            month += 1
        if preview_balance <= 0:
            print('Lowest Payment: %d' % monthlyPayment)
            break
        else:
            monthlyPayment += 10


def debt_payoff_year_calculation_bisection(balance, annualInterestRate):
    """

    :param balance: (int lub float) kwota kredytu do splacenia
    :param annualInterestRate: (int lub float) stopa procentowa odsetek w skali roku
    :return: Program wylicza kwote miesiecznej raty w celu splacenia calego kredytu w ciagu 1 roku \
    ta wersja wykorzystuje algorytm binarny
    """
    monthlyInterestRate = annualInterestRate / 12.0
    low = balance / 12.0
    high = (balance * (1 + monthlyInterestRate)**12) / 12.0
    while True:
        monthlyPayment = (low + high) / 2.0
        month = 0
        preview_balance = balance
        while month < 12:
            monthlyUnpaidBalance = preview_balance - monthlyPayment
            preview_balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
            month += 1
        if round(preview_balance, 2) > 0:
            low = monthlyPayment
        elif round(preview_balance, 2) < 0:
            high = monthlyPayment
        else:
            print('Lowest Payment: %.2f' % monthlyPayment)
            break
