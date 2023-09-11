"""
Задание №3.
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class People:
    def __init__(self, first_name: str, second_name: str, age: int):
        self.first_name = first_name
        self.second_name = second_name
        self._age = age

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, second_name: str):
        self._second_name = second_name

    @property
    def age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        print(f'Имя: {self.first_name}\nФамилия: {self.second_name}\nВозраст: {self.age}')

