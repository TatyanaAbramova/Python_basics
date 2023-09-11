"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

number = int(input('Введите целое число: '))


def convert_to(number, base=16, upper=False):
    digits = '0123456789abcdef'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


print(f'Шестнадцатеричное строковое представление введенного числа: {convert_to(number)}')
print(f'Проверка: {hex(number)}')
