# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.

# 1. + Добавьте к ним логирование ошибок и полезной информации.
# 2. + Также реализуйте возможность запуска из командной строки с передачей параметров

import argparse
import logging
import pathlib
from pprint import pprint
from collections import namedtuple

logging.basicConfig(filename = 'home01.log', filemode='w', encoding='utf-8',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

DIRSUBJECT = namedtuple('Dirsubject',['filename', 'extention', 'dir_flag', 'parent_name'])

def dir_info(path):
    dir_list = []
    logger.info(f'Корневая папка {path}')
    path = pathlib.Path(path)
    for file in path.iterdir():
        dir_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))
        logger.info(f'Добавляем в список {DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent)}')
    return dir_list

def parser():
    """Добавили парсер"""
    parser = argparse.ArgumentParser(description='path parser')
    # Добавили тип аргумента и значение по умолчанию
    parser.add_argument('-p','--path', default = r'E:\DCDownloads\GeekBrains\python')
    args = parser.parse_args()
    return dir_info(f'{args.path}')

if __name__ == '__main__':
    # Проверка работы модуля dir_info в IDE
    # pprint(dir_info(r'C:\Users'))

    # Проверка работы модуля dir_info в командной строке
    # python Seminar15/home01.py -p C:\Users\Zareff\Desktop\Learning\Python\DeepLearning\Seminar10

    pprint(parser())
