"""
✔ Напишите функцию, принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""


def hashable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(hashable_dicts(dog='Шарик', cat={'Леопольд': 2, 'Мурка': 3}, turtle=['Билл', 'Ящер', 'Толик'],
                     hamster={'Эдуард', 'Хомка'}))
