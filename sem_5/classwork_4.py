"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите числа, сумма цифр которых равна 8.
✔ Решение в одну строку
"""
# from typing import Any, Generator


def gen_num():
    return (i for i in range(0, 101, 2) if i // 10 + i % 10 != 8)


for i in gen_num():
    print(i)
