# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for a in [[2, 3, 4, 5], [6, 7, 8, 9]]:
    if a != 0:
        print('')
        for b in range(2, 10):
            print('%s * %s = %s\t\t' % (a[0], b, a[0] * b),
                  '%s * %s = %s\t\t' % (a[1], b, a[0] * b),
                  '%s * %s = %s\t\t' % (a[2], b, a[0] * b),
                  '%s * %s = %s\t\t' % (a[3], b, a[0] * b), )
