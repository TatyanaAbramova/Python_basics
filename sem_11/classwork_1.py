"""
Задание №1.
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""

from time import time


class MyStr(str):
    """Класс, где доступны все возможности str"""
    def __new__(cls, value, author):
        """Добавляет новые параметры - автор текста и время создания в класс str"""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    def __str__(self) -> str:
        return f'Экземпляр класса MyStr добавляет новые параметры author и creation time в класс str'

    def __repr__(self) -> str:
        return f'MyString({self.author=})'


if __name__ == '__main__':
    s = MyStr('hello', 'Дмитрий')
    print(f'Текст: {s}, Автор: {s.author}')
    print(f'{s.upper()}')
    print(s.time)
    print(s)
    print(f'{s = }')
    # help(MyStr)
