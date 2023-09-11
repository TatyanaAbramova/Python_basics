"""
Задание №2.
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length: float, width: float = 0):
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
        if self.__perimetr is None:
            self.__perimetr = (self.length + self.width) * 2
        return self.__perimetr

    @property
    def area(self) -> float:
        if self.__area is None:
            self.__area = self.length * self.width
        return self.__area


