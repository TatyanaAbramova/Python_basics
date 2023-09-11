# Программа угадывает число от 0 до 1000. Необходимо угадать число за 10 попыток

print('Программа угадывает число от 0 до 1000 не более чем за 10 попыток. Проверим?')
guessed = False
attempts = 0
left = 0
right = 1001

while not guessed:
    number = (left + right) // 2
    print(f'Это число {number}?')
    answ = input(': ')
    if not answ in ('<', '>', '='):
        print("Неверный ввод")
        continue
    if answ == '<':
        right = number
    elif answ == '>':
        left = number
    else:
        guessed = True
    attempts += 1

print('Компьютер угадал загаданное число за", attempts, "попыток!')
