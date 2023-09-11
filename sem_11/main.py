from classwork_1 import MyStr
from classwork_2_4 import Archive
from classwork_5_6 import Rectangle
from homework import Matrix

if __name__ == "__main__":
    """запуск classwork_1"""
    s = MyStr('hello', 'Дмитрий')
    print(f'Текст: {s}, Автор: {s.author}')
    print(f'{s.upper()}')
    print(s.time)
    print(s)
    print(f'{s = }')
    # help(MyStr)
    """запуск classwork_2_4"""
    d1 = Archive(1, 'a')
    print(d1.count, d1.text, d1.arc_counts, d1.arc_texts)
    print(f'{d1}')
    print(f'{d1 =}')
    d2 = Archive(2, 'b')
    print(d2.count, d2.text, d1.arc_counts, d1.arc_texts)
    print(f'{d2}')
    print(f'{d2 =}')
    d3 = Archive(3, 'c')
    print(d3.count, d3.text, d2.arc_counts, d2.arc_texts)
    """запуск classwork_5_6"""
    rectangle1 = Rectangle(6)
    print(f'Длина первого прямоугольника: {rectangle1.width}')
    print(f'Ширина первого прямоугольника: {rectangle1.length}')
    print(f'Периметр первого прямоугольника: {rectangle1.perimetr}')
    print(f'Площадь первого прямоугольника: {rectangle1.area}\n')
    rectangle2 = Rectangle(4, 5)
    print(f'Длина второго прямоугольника: {rectangle2.width}')
    print(f'Ширина второго прямоугольника: {rectangle2.length}')
    print(f'Периметр второго прямоугольника: {rectangle2.perimetr}')
    print(f'Площадь второго прямоугольника: {rectangle2.area}\n')
    new_rec = rectangle1 + rectangle2
    print(f'Длина нового прямоугольника: {new_rec.width}')
    print(f'Ширина нового прямоугольника: {new_rec.length}')
    print(f'Периметр нового прямоугольника: {new_rec.perimetr}')
    print(f'Площадь нового прямоугольника: {new_rec.area}\n')
    compare_rec = rectangle1 - rectangle2
    print(f'Разница длины прямоугольников: {compare_rec.length}'),
    print(f'Разница ширины прямоугольников: {compare_rec.width}'),
    print(f'Разница периметров прямоугольников: {compare_rec.perimetr}')
    print(f'Разница площадей прямоугольников: {rectangle1.area - rectangle2.area}')
    """запуск homework"""
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'Первая матрица: \n{matrix_1}\n')
    print(f'Вторая матрица: \n{matrix_2}\n')
    print(f'Третья матрица: \n{matrix_3}\n')

    print(f'Матрица 1 равна матрице 2? --> {matrix_1 == matrix_2}\n', )
    print(f'Матрица 1 равна матрице 3? --> {matrix_1 == matrix_3}\n', )

    print(f'Матрица 1 меньше матрицы 2? --> {matrix_1 < matrix_2}\n', )
    print(f'Матрица 1 больше матрицы 2? --> {matrix_1 > matrix_2}\n', )

    print(f'Сумма матриц 1 и 2: \n{matrix_1 + matrix_2}\n', )
    print(f'Сумма матриц 1 и 3: \n{matrix_1 + matrix_3}\n', )
    print(f'Сумма матриц 2 и 3: \n{matrix_2 + matrix_3}\n', )

    print(f'Произведение матриц 1 и 2: \n{matrix_1 * matrix_2}\n', )
    print(f'Произведение матриц 1 и 2: \n{matrix_1 * matrix_2}\n', )
    print(f'Произведение матриц 1 и 2: \n{matrix_1 * matrix_2}\n', )

