# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)


# import time
#
#
# class MyString(str):
# def __new__(cls, value, author=None):
# return super().__new__(cls, value)
#
# def __init__(self, value, author=None):
# self.author = author
# self.time = time.time()
#
#
# my_string = MyString('строка', 'Стоун')
# print(my_string)
# print(my_string.author)
# print(my_string.time)



# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# class Archive:
# archive = []
#
# def __new__(cls, digit, letter):
# instance = super().__new__(cls)
# instance.digit = digit
# instance.letter = letter
# instance.archive = cls.archive.copy()
# cls.archive.append(instance)
# return instance
#
# def __repr__(self):
# return f'{self.digit} {self.letter}'
#
#
# a = Archive(1, 'A')
# b = Archive(2, 'B')
# c = Archive(3, 'C')
# d = Archive(4, 'D')
#
# print(a)
# print(a.archive)
# print(b)
# print(b.archive)
# print(c)
# print(c.archive)
# print(d)
# print(d.archive)


# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# class Rectangle:
# def __init__(self, length, width=None):
# self.length = length
# self.width = width if width else length
# 
# def perimeter(self):
# return 2 * self.length + 2 * self.width
#
# def area(self):
# return self.width * self.length
#
# def __add__(self, other):
# if isinstance(other, Rectangle):
# new_width = self.width + other.width
# new_length = self.length + other.length
# return Rectangle(new_width, new_length)
# raise TypeError
#
# def __sub__(self, other):
# if isinstance(other, Rectangle):
# if self.width > other.width and self.length > other.length:
# new_width = self.width - other.width
# new_length = self.length - other.length
# return Rectangle(new_width, new_length)
# raise ValueError
# raise TypeError
#
#
# def __str__(self):
# return f'{self.length=} {self.width=}'
#
#
# r1=Rectangle(6,7)
# r2=Rectangle(3,4)
#
# print(r1+r2)
# print(r1-r2)
