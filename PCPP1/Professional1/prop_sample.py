
class AccountException(Exception):
    pass

class BankAccount:

    def __init__(self) -> None:
        self.__balance = 0.

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise AccountException('Can\'t set negative amount to account balance.')

        self.__balance = amount

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise AccountException('Can\'t delete account with values.')
        self.__balance = 0.

    def deposit(self, amount: float):
        if amount > 100000:
            print('Deposit over 100.000')
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > 100000:
            print('Withdraw over 100.000')
        self.__balance -= amount

a = BankAccount()
a.balance = 1000

try:
    a.balance = -200
except Exception as e:
    print(e)

a.deposit(1000000)
try:
    del a.balance
except Exception as e:
    print(e)