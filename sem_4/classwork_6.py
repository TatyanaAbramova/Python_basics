"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""


def list_sum(numbers: list[int], index_1: int, index_2: int) -> int:
    index_1 = index_1 if index_1 >= 0 else 0
    index_2 = index_2 if index_2 <= len(numbers) else len(numbers)
    result = 0
    for i in numbers[index_1:index_2]:
        result += i
    return result


nums = [1, 2, 3, 4, 5, 6, 7]
i_1 = 2
i_2 = 5
print('Сумма чисел между переданными индексами:', list_sum(nums, i_1, i_2))
