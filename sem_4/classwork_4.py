"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
"""


def bubble_sort(inp: list[int]) -> list[int]:
    # Внешний цикл для обхода всего списка
    for i in range(0, len(list_1) - 1):
        for j in range(len(list_1) - 1):
            if list_1[j] > list_1[j + 1]:
                temp = list_1[j]
                list_1[j] = list_1[j + 1]
                list_1[j + 1] = temp
    return list_1


list_1 = [5, 4, 3, 1, 2]
print('Исходный список чисел: ', list_1)
print('Отсортированный список: ', bubble_sort(list_1))

