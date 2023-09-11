from classwork_1 import Circle
from classwork_2 import Rectangle
from classwork_3 import People
from classwork_4 import Worker
from classwork_5 import Fish, Cat, Dog
from homework_1 import AnimalFabric
from homework_2 import CreateFileWithNumbers, GenerateFileWithNames, GenerateFileWithMultiplication

if __name__ == '__main__':
    """classwork_1"""
    new_circle = Circle(int(input('Введите значение радиуса: ')))
    print(f'Длина окружности = {round(new_circle.circle_long, 3)}')
    print(f'Площадь окружности = {round(new_circle.area, 3)}')
    """classwork_2"""
    new_rectangle = Rectangle(1, 2)
    print(new_rectangle.perimetr)
    print(new_rectangle.area)
    """classwork_3"""
    man = People(first_name=input('Введите имя: '),
                 second_name=input('Введите фамилию: '),
                 age=int(input('Введите возраст: ')))

    man.birthday()
    print(f'{man.first_name} празднует день рождения, исполнилось {man.age}')
    man.full_name()
    """classwork_4"""
    man = Worker(first_name=input('Введите имя: '),
                 second_name=input('Введите фамилию: '),
                 age=int(input('Введите возраст: ')))

    man.full_name()
    print(f'Идентификационный номер: {man.worker_id}')
    print(f'Уровень доступа: {man.secure_lvl}')
    """classwork_5"""
    fish = Fish(True, 'Немо', 'Рыба-меч')
    cat = Cat(False, 'Барсик', 'Персидский кот')
    dog = Dog('Шарик', 'Tакса')
    dog.commands = ['Рядом!', 'Фас!']
    fish.get_uniq_attr()
    cat.get_uniq_attr()
    dog.get_uniq_attr()
    """homework_1"""
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal('dog', 'Шарик', 'Такса')
    animal_from_fabric.commands = ['Рядом!', 'Фас!']
    print(animal_from_fabric)
    """homework_2"""
    test1 = CreateFileWithNumbers(10, "test.txt")
    test1.numbers_file()
    print(test1.name)

    test2 = GenerateFileWithNames(10, "names.txt")
    test2.generate_names()
    print(test2.names)

    test3 = GenerateFileWithMultiplication(test1.name, test2.names, 'new_file.txt')
    test3.multiplying()