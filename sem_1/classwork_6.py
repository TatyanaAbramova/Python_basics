# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif.
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

CHECK_1 = 4
CHECK_2 = 100
CHECK_3 = 400
START_YEAR = 1582
result = ''
year = int(input('Введите год: '))
if year < START_YEAR:
    result = 'Введите год начиная с 1582'
elif year % CHECK_1:
    result = 'Год обычный'
elif not year % CHECK_2:
    if not year % CHECK_3:
        result = 'Год високосный'
    else:
        result = 'Год обычный'
else:
    result = 'Год обычный'
print(result)
