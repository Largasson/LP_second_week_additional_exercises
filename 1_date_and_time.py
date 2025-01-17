import datetime
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    td = datetime.date.today()
    print(f"Сегодня: {td}")
    print(f"Вчера: {td - datetime.timedelta(days=1)}")
    print(f"30 дней назад: {td - datetime.timedelta(days=30)}")

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    d = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return d

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
