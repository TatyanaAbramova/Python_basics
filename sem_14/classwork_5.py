"""
## Задание №5.
* На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
* Напишите 3-7 тестов unittest для данного класса.
"""

import unittest
import pytest
from functools import total_ordering


@total_ordering
class Rectangle:
    """Класс вычисляет периметр и площадь прямоугольника, а также складывает и вычитает периметры"""

    def __init__(self, length: float, width: float = 0):
        """Добавляет параметр длины и ширины, если добавляется только один параметр,
                    считаем, что длина и ширина равны"""
        self.length: float = length
        self.width: float = [width, length][width == 0]
        self.__perimetr: (float, None) = None
        self.__area: (float, None) = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length: float):
        self._length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width: float):
        self._width = width

    @property
    def perimetr(self) -> float:
        """Вычисляем периметр прямоугольника"""
        if self.__perimetr is None:
            self.__perimetr = (self.length + self.width) * 2
        return self.__perimetr

    @property
    def area(self) -> float:
        """Вычисляем площадь прямоугольника"""
        if self.__area is None:
            self.__area = self.length * self.width
        return self.__area

    def __add__(self, other):
        """Складываем периметры прямоугольников"""
        new_perimetr = self.perimetr + other.perimetr
        new_length = self.length + other.length
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """Вычитаем периметры прямоугольников"""
        new_perimetr = abs(self.perimetr - other.perimetr)
        new_length = abs(self.length - other.length)
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle1 = Rectangle(2, 3)
        self.rectangle2 = Rectangle(5, 10)
        self.rectangle3 = Rectangle(5)

    def test_perimeter(self):
        self.assertEqual(self.rectangle1.perimetr, 10)

    def test_area(self):
        self.assertEqual(self.rectangle2.area, 50)

    def test_sum_rect(self):
        self.assertEqual((self.rectangle1 + self.rectangle2).perimetr, 40)

    def test_str(self):
        self.assertEqual(self.rectangle1.__str__(), 'Прямоугольник 2 x 3')


if __name__ == '__main__':
    # rectangle1 = Rectangle(6)
    # print(f'Длина первого прямоугольника: {rectangle1.width}')
    # print(f'Ширина первого прямоугольника: {rectangle1.length}')
    # print(f'Периметр первого прямоугольника: {rectangle1.perimetr}')
    # print(f'Площадь первого прямоугольника: {rectangle1.area}\n')
    # rectangle2 = Rectangle(4, 5)
    # print(f'Длина второго прямоугольника: {rectangle2.width}')
    # print(f'Ширина второго прямоугольника: {rectangle2.length}')
    # print(f'Периметр второго прямоугольника: {rectangle2.perimetr}')
    # print(f'Площадь второго прямоугольника: {rectangle2.area}\n')
    # new_rec = rectangle1 + rectangle2
    # print(f'Длина нового прямоугольника: {new_rec.width}')
    # print(f'Ширина нового прямоугольника: {new_rec.length}')
    # print(f'Периметр нового прямоугольника: {new_rec.perimetr}')
    # print(f'Площадь нового прямоугольника: {new_rec.area}\n')
    # compare_rec = rectangle1 - rectangle2
    # print(f'Разница длины прямоугольников: {compare_rec.length}'),
    # print(f'Разница ширины прямоугольников: {compare_rec.width}'),
    # print(f'Разница периметров прямоугольников: {compare_rec.perimetr}')
    # print(f'Разница площадей прямоугольников: {rectangle1.area - rectangle2.area}')

    # unittest.main(verbosity=True)
    pytest.main(['-v'])
