"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


def cash_bonus(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


names_ = ["Иванов", "Петров", "Сидоров"]
cash_ = [70000, 90000, 58000]
bonus = ["10.25%", "9.0%", "13.0%"]
print(cash_bonus(names_, cash_, bonus))

