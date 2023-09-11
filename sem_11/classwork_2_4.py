"""
Задание №2.
* Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
* При запуске нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра.

Задание №3.
* Добавьте к задачам 1 и 2 строки документации для классов
"""


class Archive:
    """Класс хранит пару значений - число и строку."""
    instance = None
    arc_counts = []
    arc_texts = []

    def __init__(self, count, text):
        """Добавляет новые значения"""
        self.count = count
        self.text = text

    def __new__(cls, *args, **kwargs):
        """Добавляет ранее созданные значения в архив"""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.arc_counts.append(cls.instance.count)
            cls.instance.arc_texts.append(cls.instance.text)
        return cls.instance

    def __str__(self):
        c = self.instance.arc_counts if self.instance.arc_counts else 'Пусто'
        t = self.instance.arc_texts if self.instance.arc_texts else 'Пусто'
        return f'Число: {self.instance.count}, Текст: {self.instance.text}, Архив чисел: {c}, Архив текста: {t}'

    def __repr__(self):
        return f' Архив: ({self.instance.count}, {self.instance.text})'


if __name__ == '__main__':
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
