"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных,
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def replacement_s(*variables):
    variables = list(variables)
    temp = []
    for i in range(len(variables)):
        if variables[i].endswith('s') and variables[i] != 's':
            temp.append(variables[i])
            variables[i] = None
    for i in range(len(variables)):
        if variables[i] is not None:
            variables[i] += ''.join([i for i in temp])
    return variables


print(replacement_s('focus', 'post', 'wheel', 's'))