from bank_account import BankAccount
import random
import json
import os
class Bank:
    """
    The Bank class represents a financial institution that manages multiple bank accounts. It serves
    as a central hub for handling account creation, deletion, retrieval, and transfers between
    accounts.
    """
    def __init__(self):
        self.__accounts = {}

    def load(self):
        path = ".venv/bank.json"
        if os.path.exists(path):
            with open(path, "r") as file:
                self.__accounts = json.load(file)
            for key, values in self.__accounts.items():
                self.__accounts[key] = BankAccount(values["holder"], values["number"],
                                                   values["balance"], values["password"],
                                                   values["email"])
            self.__accounts = {int(k): v for k, v in self.__accounts.items()}  ##json converts int keys into strings (took me 1.5 hours to realize ts)
        else:
            with open(path, "w") as file:
                json.dump(self.__accounts, file)

    def save(self):
        for key, values in self.__accounts.items():
            self.__accounts[key] = values.to_dict()
        with open('.venv/bank.json', "w") as file:
            json.dump(self.__accounts, file)

    def add_account(self):
        holder = input("Enter account holder name: ").strip()
        while holder.isdigit():
            print("Account holder name must only contain alphabets!")
            holder = input("Enter account holder name: ").strip()
        password = input("Enter account password: ")
        while len(password) < 8:
            print("Password must be at least 8 characters long!")
            password = input("Enter account password: ")
        email = input("Enter account email: ")
        number = self.generate_randint()
        self.__accounts[number] = BankAccount(holder, str(number), 0, password, email)
        print(f"Bank account of {holder} successfully created. Bank account number: {number}")
        return True

    def retrieve_account_int(self, num: int):
        """Retrieve account by account number"""
        if num in self.__accounts:
            return self.__accounts[num]
        else:
            return False

    def retrieve_account_str(self, name: str):
        """Retrieve account by account holder"""
        acc = []
        for obj in self.__accounts.values():
            if obj.account_holder == name:
                acc.append(str(obj))
        if len(acc) == 0:
            return False
        else:
            return acc

    def reset_password(self, password: str, account_number: str):
        account = None
        for values in self.__accounts.values():
            if values.account_number == account_number:
                account = values
        if account is None:
            print("Account does not exist!")
            return False
        account.password = password
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return True

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
            print(f"{key}: {instance.account_holder}")
        print("End of list. \n")
        return True

    def transfer_amount(self, account1: str, account2: str, amount):
        """Transfers amount from account 1 to account 2 (pass holder name as arg)"""
        acc1_obj, acc2_obj = None, None
        for values in self.__accounts.values():
            if values.account_number == account1:
                acc1_obj = values    #reassign account1 to BankAccount instance
            if values.account_number == account2:
                acc2_obj = values
        if acc2_obj is None:
            print("Account 2 holder name does not exist!")
            return False
        elif acc1_obj is None:
            print("Account 1 holder name does not exist!")
            return False
        if acc1_obj.withdraw(amount):
            acc2_obj.deposit(amount)
        else:
            print("Transfer failed.")

    def retrieve_email(self, account_number: str):
        account = None
        for values in self.__accounts.values():
            if values.account_number == account_number:
                account = values
        if account is None:
            print("Account does not exist!")
            return False
        if not account.try_password():
            return False
        print(account.email)
        return True

    def debug(self):
        """Used for debugging only"""
        for keys in self.__accounts.keys():
            print(type(keys))

    def to_int_debug(self):
        """Convert all dictionary keys to integers if they are strings. (used for debugging)"""
        self.load()

        self.save()


if __name__ == "__main__":
    bank = Bank()
    bank.load()
    print(bank.list_accounts())

    bank.debug()

