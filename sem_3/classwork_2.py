"""
Задание №2 Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

text = input('Введите данные: ')
res = None
if ('.' in text or (text.count('-') and text.index('-') == 0)) and \
        text.replace('.', '').replace('-', '').isdigit():
    res = float(text)
elif text.isdigit():
    res = int(text)
elif text.lower() != text:
    res = text.lower()
else:
    res = text.upper()

print(res)
