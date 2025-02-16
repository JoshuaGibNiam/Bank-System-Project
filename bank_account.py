class BankAccount:
    """Manages individual bank accounts"""
    def __init__(self, account_holder: str, account_number: int):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = 0

    def get_account_holder(self) -> str:
        return self.__account_holder

    def get_account_number(self) -> int:
        return self.__account_number

    def get_balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int):
        self.__balance += amount if amount > 0 else 0

    def withdraw(self, amount: int):
        self.__balance -= amount if amount < 0 and self.__balance > amount else 0

