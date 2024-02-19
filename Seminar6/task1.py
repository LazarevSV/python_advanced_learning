
# Проверка корректности даты
#
# Инструкция по использованию платформы
#
#
#
# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в
# зависимости от результата проверки.
#
# Пример использования На входе:
#
#
# date_to_prove = 15.4.2023
# На выходе:
#
#
# True









#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно -
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

date_to_prove = 15.4,2023

from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))