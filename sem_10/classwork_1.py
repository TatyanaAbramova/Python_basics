"""
Задание №1.
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""


from math import pi
import decimal


class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius
        self.__circle_long: (decimal, None) = None
        self.__square: (decimal, None) = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        self._radius = radius

    @property
    def circle_long(self) -> decimal:
        if self.__circle_long is None:
            self.__circle_long = decimal.Decimal(pi * self.radius * 2)
        return self.__circle_long

    @property
    def area(self) -> decimal:
        if self.__square is None:
            self.__square = decimal.Decimal(pi * pow(self.radius, 2))
        return self.__square



