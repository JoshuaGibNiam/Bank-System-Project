from bank_account import BankAccount
import random
class Bank:
    """
    The Bank class represents a financial institution that manages multiple bank accounts. It serves
    as a central hub for handling account creation, deletion, retrieval, and transfers between
    accounts.
    """
    def __init__(self):
        self.__accounts = {}

    def add_account(self):
        holder = input("Enter account holder name: ").strip()
        while not holder.isalpha():
            print("Account holder name must only contain alphabets!")
            holder = input("Enter account holder name: ").strip()
        number = self.generate_randint()
        self.__accounts[number] = BankAccount(holder, str(number), 0)
        print(f"Bank account of {holder} successfully created.")
        return True

    def retrieve_account(self, num):
        return self.__accounts[num]

    def delete_account(self, num):
        del self.__accounts[num]
        print(f"Bank account {num} deleted.")
        return True

    def generate_randint(self):
        number = random.randint(1, 100000)
        while number in self.__accounts:
            number = random.randint(1, 100000)
        return number

    def list_accounts(self):
        print("Active bank accounts:")
        for key, instance in self.__accounts.items():
            print(f"{key}: {instance.get_account_holder()}")
        print("End of list. \n")
        return True

    def transfer_amount(self, account1, account2, amount):
        """Transfers amount from account 1 to account 2 (pass holder name as arg)"""
        for values in self.__accounts.values():
            if values.get_account_holder() == account1:
                account1 = values    #reassign account1 to BankAccount instance
            if values.get_account_holder() == account2:
                account2 = values
        if account1.withdraw(amount):
            account2.deposit(amount)
        else:
            print("Transfer failed.")
