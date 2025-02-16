class BankAccount:
    """Manages individual bank accounts"""
    def __init__(self, account_holder: str, account_number: int, initial_balance: float):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_holder(self) -> str:
        """Returns the account holder in a string"""
        return self.__account_holder

    def get_account_number(self) -> float:
        """Returns the account number in a float"""
        return self.__account_number

    def get_balance(self) -> int:
        """Returns the account balance in a float"""
        return self.__balance

    def deposit(self, amount: int):
        """Deposits an amount into the account, checks if the deposit is positive"""
        self.__balance += amount if amount > 0 else 0

    def withdraw(self, amount: int):
        """Withdraws an amount from the account, checks if the withdrawal is possible"""
        self.__balance -= amount if amount < 0 and self.__balance > amount else 0

