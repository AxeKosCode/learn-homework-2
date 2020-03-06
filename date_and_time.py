"""
Домашнее задание №2
Дата и время
* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    today = datetime.now()  #текущая дата на сегодня
    today_f = today.strftime('%d.%m.%Y')    #отформатированная дата
    yestoday = today - timedelta(days=1)   #вчерашняя дата
    yestoday_f = yestoday.strftime('%d.%m.%Y')  #отформатированная дата
    month_to_back = today - timedelta(days=365/12)  #дата на месяц назад
    month_to_back_f = month_to_back.strftime('%d.%m.%Y')    #отформатированная дата

    print('Сегодня', today_f)
    print('Вчера было', yestoday_f)
    print('Месяц назад было', month_to_back_f)
    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    new_date = datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
    return new_date

if __name__ == "__main__":
    print_days()
    print()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
    print(str_2_datetime("31/12/07 07:25:58.0011"))
    print(str_2_datetime("10/09/33 15:33:13.325"))
