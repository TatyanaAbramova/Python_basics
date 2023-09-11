# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# 	num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


def guess_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    COUNT_TRY = 10
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    is_win = True
    for _ in range(COUNT_TRY + 1):
        number = int(input('Введи число от 0 до 1000: '))
        if number > num:
            print('Ваше число БОЛЬШЕ загаданного')
            is_win = False
        elif number < num:
            print('Ваше число МЕНЬШЕ загаданного')
            is_win = False
        else:
            print('Вы выиграли!')
            is_win = True
            break
    if not is_win:
        print('К сожалению вы проиграли')


guess_number()
