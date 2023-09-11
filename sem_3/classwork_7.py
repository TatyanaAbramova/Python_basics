"""
Задание №7
✔ Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в
строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ — символ,
а значение — частота встречи символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.
"""


# 7.1


def chr_dict(text: str) -> dict[str:int]:
    return {char: text.count(char) for char in text}


text_1 = "А роза упала на лапу Азора"

[print(f"{key}: {value}") for key, value in chr_dict(text_1).items()]

# 7.2


text_2 = 'А роза упала на лапу Азора'

dict_of_char = {}
for i in text_2:
    if i in dict_of_char.keys():
        dict_of_char[i] += 1
    else:
        dict_of_char[i] = 1
print(dict_of_char)
