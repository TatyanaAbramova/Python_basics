""" 
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. 
"""

from typing import Callable


def closure_function_game(guess_num: int, count: int) -> Callable[[], None]:
    def wrapper():
        for i in range(1, count + 1):
            print(f'Попытка № {i} ')
            user_num = int(input('Введите число от 1 до 100: \n >>> '))
            if user_num == guess_num:
                print("Угадал!!!")
                break
            elif user_num < guess_num:
                print('Хозяин, нужно больше золота :)')
            else:
                print('Перебор ;)')
    return wrapper






