"""
Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили. Сохраните его итератор.
✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
"""


def from_str_to_dict_2(text_2: str) -> dict[str:int]:
    res_iter = iter({k: ord(k) for k in text_2}.items())
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))


from_str_to_dict_2('Дима')
