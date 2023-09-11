"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел, начиная с числа 2.
✔ Для проверки числа на простоту используйте правило:
«число является простым, если делится нацело только на единицу и на себя».
"""


# def prime_gen(n: int) -> (iter, int):
#     primes_list = []
#     current_number = 2
#     while len(primes_list) < n:
#         is_prime = True
#         for num in primes_list:
#             if current_number % num == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes_list.append(current_number)
#             yield current_number
#         current_number += 1
#
#
# def func_2(input_number):
#     result = True
#     for divider in range(2, input_number+1):
#         if input_number % divider == 0:
#             result = False  # при первом же делении нацело возвращаем не простое
#             break
#     yield result


def simple_numbers(number: int):
    yield 2
    for i in range(3, number + 1):
        simple = True
        for j in range(2, i - 1):
            if not i % j:
                simple = False
        if simple:
            yield i


print(*simple_numbers(20))