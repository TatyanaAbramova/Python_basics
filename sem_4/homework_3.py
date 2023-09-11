def _exit():
    return "Всего доброго, приходите к нам еще"


class Bank:
    _BALANCE = 0
    _MIN = 50
    _MAX = 5000000
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int, tax: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash + tax
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _out(self, cash: int, commission: int, tax: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission + tax) >= 0:
            self._BALANCE -= cash + commission + tax
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION
        _MAX = 600
        _MIN = 30
        if sum_commission > _MAX:
            sum_commission = _MAX
        elif sum_commission < _MIN:
            sum_commission = _MIN
        else:
            sum_commission = int(sum_commission)
        return sum_commission

    def _check_tax(self, cash: int) -> float | int:
        if cash >= self._MAX:
            print(f'\nВнимание был снят налог на богатство в размере {cash * self._TAX}')
            return cash * self._TAX
        else:
            return 0

    def add_bonus(self):
        self._BALANCE += self._BALANCE * self._BONUS
        return f'Поздравляем, вы получили бонус за каждую 3-ю операцию в нашем банке. ' \
               f'На ваш счет было зачислено: {int(self._BALANCE * self._BONUS)}\n'

    def start(self, mode: str, cash: int = 0) -> str:
        if self._OPERATION % 3 == 0:
            print(self.add_bonus())
        tax = self._check_tax(cash)
        match mode:
            case "in":
                self._in(cash=cash, tax=tax)
                return f"Средства были зачислены сумма: {cash}, баланс: {int(self._BALANCE)}"
            case "out":
                commission = self._check_commission(cash=cash)
                data = self._out(cash=cash, commission=commission, tax=tax)
                if data:
                    return f"Операция осуществлена успешно, сумма: {cash}, комиссия: {commission}, " \
                           f"баланс: {int(self._BALANCE)}"
                else:
                    return "Не хватает средств"

            case "exit":
                return _exit()


bank = Bank()
print(bank.start(mode='in', cash=400))
print(bank.start(mode='in', cash=10000))
print(bank.start(mode='out', cash=1000))
print(bank.start(mode='in', cash=100))
print(bank.start(mode='in', cash=1000))
print(bank.start(mode='in', cash=2000))
print(bank.start(mode='out', cash=5000))