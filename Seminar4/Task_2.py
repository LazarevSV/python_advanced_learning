# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
#
#
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
#
#
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
#
def key_params(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, str, float, bool, tuple)):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict


print(key_params(a = True, b = False, c = True, d = False))
print(key_params(a = 1, b = 'hello', c = [1, 2, 3], d = {}))
print(key_params(a = 42, b = 'hello', c = 3.14, d = 'world'))
print(key_params(a = None, b = '', c = [], d = {}))
print(key_params(name = 'Alice', age = 30, scores = [85, 90, 78], info = {'city': 'New York', 'email': 'alice@example.com'}))