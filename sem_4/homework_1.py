"""
✔ Напишите функцию для транспонирования матрицы
Матрица транспонированной данной, получается из исходной путем
замены каждой ее строки столбцом с этим же номером. Обозначается такая матрица A^T или A'
"""


def transparent_matrix(*a_list: list[[int]]) -> list[()] | str:
    is_transparent = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_transparent = False
    if is_transparent:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспонировать'


print(transparent_matrix([1, 2], [3, 4]))
