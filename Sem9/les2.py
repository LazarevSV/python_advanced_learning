# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
from random import randint as ri

MIN_LIMIT = 1
MAX_LIMIT = 100
MIN_COUNT = 1
MAX_COUNT = 10


def game_rules(func):


    def inner(number, count):


user_number = number if MIN_LIMIT <= number <= MAX_LIMIT else ri(MIN_LIMIT, MAX_LIMIT)
user_count = count if MIN_COUNT <= count <= MAX_COUNT else ri(MIN_COUNT, MAX_COUNT)
func(user_number, user_count)
return inner


@game_rules
def guess_game(user_number, user_count):


while user_count:
    guess_num = int(input(f'Угадайте число от {MIN_LIMIT} до {MAX_LIMIT}: '))
if guess_num == user_number:
    print(f'Ура, ты победил! Это число {user_number}')
return
elif guess_num < user_number:
print('Загаданное число больше!')
else:
print('Загаданное число меньше!')
user_count -= 1
print(f'Увы! Ты проиграл! Это было число {user_number}!')

if __name__ == '__main__':
    guess_game(17, 7)
