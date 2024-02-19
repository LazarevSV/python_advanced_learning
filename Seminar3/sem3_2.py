
import re
from collections import Counter

# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов.
#
# Пример
#
# На входе:
#
#
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
#
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]



def get_top_words(text, top_n=10):
    # Приводим текст к нижнему регистру
    text = text.lower()

    # Заменяем апострофы на пробелы, чтобы разделить слова с апострофами
    text = text.replace("'", " ")

    # Убираем знаки препинания, разделяем слова пробелами
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    # Считаем количество повторяющихся слов
    word_counts = Counter(words)

    # Получаем топ N слов
    top_words = word_counts.most_common(top_n)

    return top_words


# Пример использования
text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
result = get_top_words(text, top_n=10)
print(result)

# [('python', 2), ('is', 1), ('the', 1), ('latest', 1), ('version', 1), ('of', 1), ('it', 1), ('s', 1), ('awesome', 1)]

