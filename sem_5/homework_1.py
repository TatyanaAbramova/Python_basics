"""
Задание №1
✔ Напишите функцию, которая принимает на вход
строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


file_p = '/Users/dima4/python_basics/sem_5/README.md'
print(file_info(file_p))
