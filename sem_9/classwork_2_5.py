"""
Задание №2.
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа
в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.


Задание №5.
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""


from typing import Callable
from random import randint
from classwork_4 import counts_wrap
from classwork_3 import to_json_wrapper


def closure_function_game_wrap(func) -> Callable[[], None]:
    def wrapper(guess_num: int, count: int, *args, **kwargs):
        if 1 > guess_num or guess_num > 100:
            guess_num = randint(1, 100)
        if 1 > count or guess_num > 10:
            count = randint(1, 10)
        result = func(guess_num, count, *args, **kwargs)
        return result
    return wrapper


@counts_wrap(3)
@closure_function_game_wrap
@to_json_wrapper
def game2(guess_num: int, count: int):
    for i in range(1, count + 1):
        print(f'Попытка номер {i} ')
        user_num = int(input('Введите число от 1 до 100: \n >>> '))
        if user_num == guess_num:
            print('Угадал!!!')
            break
        elif user_num < guess_num:
            print('Хозяин, нужно больше золота :)')
        else:
            print('Перебор ;)')


if __name__ == '__main__':
    game2(25, -5)

