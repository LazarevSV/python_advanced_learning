
# 📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.


# class Factorial:
# def __init__(self, limit: int):
# self.limit = limit
# self.result = []
#
# def __call__(self, count: int):
# fact = 1
# list_fact = []
# for i in range(1, count):
# fact *= i
# list_fact.append(fact)
# self.result.append(list_fact[-self.limit:])
# return fact

# *************
# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


import json

# class Factorial:
# def __init__(self, limit: int):
# self.limit = limit
# self.result = []
#
# def __call__(self, count: int):
# fact = 1
# list_fact = []
# for i in range(1, count):
# fact *= i
# list_fact.append(fact)
# self.result.append(list_fact[-self.limit:])
# return fact
#
# def __enter__(self):
# return self
#
# def __exit__(self, exc_type, exc_val, exc_tb):
# filename='result.json'
# with open(filename, 'w', encoding='utf-8') as file:
# json.dump(self.result, file)
#
#
# f1 = Factorial(3)
# with f1 as json_file:
# json_file(5)
# #



# Задание №3 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

# class FactRange:
# def __init__(self, *args):
# data = args[:3]
# self.start, self.step = 1, 1
# if len(data) == 1:
# self.stop = data[0]
# elif len(data) == 2:
# self.start, self.stop = data
# else:
# self.start, self.stop, self.step = data
# self.data = [*range(self.start, self.stop+1, self.step)]
# self.value = 1
#
# def _get_fact(self, limit):
# fact = 1
# for i in range(1, limit + 1):
# fact *= i
# self.value = fact
# return fact
#
# def __iter__(self):
# return self
#
# def __next__(self):
# if self.data:
# return self._get_fact(self.data.pop(0))
# raise StopIteration
#
# def __str__(self):
# return str(self.value)
#
#
# if __name__ == '__main__':
# factorial_gen = FactRange(5,10,3)
# for i in factorial_gen:
# print(i)

# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

# class Rectangle:
# def __init__(self, length, width=None):
# self._length = length
# self._width = width if width else length
#
# def perimeter(self):
# return 2 * self._length + 2 * self._width
#
# def area(self):
# return self._width * self._length
#
# @property
# def length(self):
# return self._length
#
# @property
# def width(self):
# return self._width
#
# @length.setter
# def length(self, value):
# if value>0:
# self._length=value
# else:
# raise ValueError ('Размер не может быть отрицательным')
#
# @width.setter
# def width(self, value):
# if value > 0:
# self._width = value
# else:
# raise ValueError('Размер не может быть отрицательным')
#
#
# rect1=Rectangle(3,4)
# rect1.length=10
# print(rect1.length)
# #rect1.width=-3


# Задание №6


# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.


class SideValidate:

def __init__(self, min_value: float = None, max_value: float = None):
self.min_value = min_value
self.max_value = max_value

def __set_name__(self, owner, name):
self.param_name = '_' + name

def __get__(self, instance, owner):
return getattr(instance, self.param_name)

def __set__(self, instance, value):
self.validate(value)
setattr(instance, self.param_name, value)

def validate(self, value):
if self.min_value is not None and value < self.min_value:
raise ValueError(f'{value} is lesser than {self.min_value}')
if self.max_value is not None and value > self.max_value:
raise ValueError(f'{value} is greater than {self.max_value}')


class Rectangle:
side_a = SideValidate(1, 20)
side_b = SideValidate(1, 15)

def __init__(self, a, b):
self.side_a = a
self.side_b = b

def __str__(self):
return f'Прямоугольник {self.side_a} x {self.side_b}'


rect_1 = Rectangle(20, 20)
print(rect_1)


ДЕСКРИПТОР - это класс который создаеться для валидации значении атрибутов наших классов
в инит передают значения

состоит из

__set_name__
def __set_name__(self, owner, name):
self.param_name = '_' + name

__get__

def __get__(self, instance, owner):
return getattr(instance, self.param_name)



__set__


def __set__(self, instance, value):
self.validate(value)
setattr(instance, self.param_name, value)