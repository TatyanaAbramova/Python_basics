"""
Задание №2.
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""


import logging
from typing import Callable

logging.basicConfig(level=logging.INFO, filename='logs_classwork_2.log', encoding='utf-8')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):
    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dct['result'] = result
        logger.info(dct)
        return result
    return wrapper


@deco_func
def any_name(num: int, *args, **kwargs):
    return num ** 2


if __name__ == '__main__':
    any_name(10, 42, 'Hello', name='Dmitry', x=3, y=True)
