class BankAccount:
    """Manages individual bank accounts"""
    def __init__(self, account_holder: str, account_number: str, initial_balance: float):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance
    def __str__(self):
        return f"BankAccount(account_holder = {self.__account_holder}, account_number = {self.__account_number}"
    def get_account_holder(self) -> str:
        """Returns the account holder in a string"""
        return self.__account_holder

    def get_account_number(self) -> int:
        """Returns the account number in a float"""
        return self.__account_number

    def get_balance(self) -> float:
        """Returns the account balance in a float"""
        return self.__balance

    def deposit(self, amount: int):
        """Deposits an amount into the account, checks if the deposit is positive
        Return True if deposit was successful, False if not"""
        if amount >= 0:
            self.__balance += amount
            print(f"Successfully deposited {amount} into the account.")
            return True
        else:
            print("Invalid amount to be deposited.")
            return False
    def withdraw(self, amount: int):
        """Withdraws an amount from the account, checks if the withdrawal is possible
        Returns True if withdrawal was successful, False if not"""
        if  amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"Successfully withdrawn {amount} from the account.")
            return True
        else:
            print("Insufficient funds / Invalid amount")
            return False




if __name__ == "__main__":
    print("TEST1: Create a new account.")
    account = BankAccount("John", "1234", 10000)
    print(account)
    account.deposit(100)
    account.get_balance()
    account.withdraw(20000)
    account.get_balance()
    account.deposit(-22)
    account.get_account_number()
