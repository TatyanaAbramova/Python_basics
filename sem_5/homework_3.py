"""
Задание №2
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibonacci(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


f = int(input("Введите длину последовательности чисел Фибоначчи: "))
print(*(fibonacci(f)))
