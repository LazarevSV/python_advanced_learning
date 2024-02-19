# #
#
# def input_numeric():
# while True:
# data = ''
# try:
# data = input('Введите число: ')
# return int(data)
# except ValueError:
# try:
# return float(data)
# except ValueError as exc:
# print('Нужно вести int или float: ' + exc.__class__.__name__)
#
#
# number = input_numeric()
# print(number)
#
# ************

# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключени

def dict_get(my_dict, my_key, default_value):
try:
return my_dict[my_key]
except KeyError as e:
return default_value


dict1 = {1: 'one', 2:'two'}

print(dict_get(dict1, 1, '0'))
print(dict_get(dict1, 3, '0'))


# 📌 Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyError(Exception):
def __init__(self, msg, message):
self.message = message
self.msg = msg

def __str__(self):
return f'{self.msg}: {self.message}'


class LevelError(MyError):
def __init__(self, message):
super().__init__('Ошибка уровня', message)


class AccessError(MyError):
def __init__(self, message):
super().__init__('Ошибка доступа', message)

raise AccessError('не хватает прав')

**************************

# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
# в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет,
# вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.




