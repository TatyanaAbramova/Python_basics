"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки, отсортированный по убыванию.
"""


def uni_code(words: str) -> list[int]:
    return sorted([ord(i) for i in set(words)], reverse=True)


text = input('Ввод текста: ')

print([f'{i} - {chr(i)}' for i in uni_code(text)])
