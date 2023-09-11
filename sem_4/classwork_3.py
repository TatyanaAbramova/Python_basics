"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""


def dict_utf_char(text: str) -> dict[str:int]:
    begin, ending = sorted([int(i) for i in text.split()])
    return {chr(i): i for i in range(begin, ending + 1)}


print(dict_utf_char(input("Введите два числа через пробел: ")))
