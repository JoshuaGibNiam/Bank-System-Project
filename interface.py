from bank import Bank

class Interface:
    def __init__(self):
        self.__bank = Bank()

    def display_main_menu(self):
        print("Welcome to Python Bank!\n"
              "Enter the following commands (1-3):\n"
              "1: Manage Accounts\n"
              "2: Bank Operations\n"
              "3. Exit bank")
    def handle_main_menu(self):
        command = input("What would you like to do?(Enter 1-3): ")
        if command == "1" or command.lower() == "manage accounts":
            self.display_account_menu()
            self.handle_account_menu()
            return True
        elif command == "2" or command.lower() == "bank operations":
            self.display_bank_menu()
            self.handle_bank_menu()
            return True
        elif command == "3" or command.lower() == "exit":
            return False
        else:
            print("Invalid command")
            return True

    def display_account_menu(self):
        print("Welcome to account management!\n"
              "Enter the following commands (1-5):\n"
              "1. View Balance\n"
              "2. Deposit Money\n"
              "3. Withdraw Money\n"
              "4. Delete Account\n"
              "5. Retrieve Account Email\n"
              "6. Reset Password\n"
              "7. Back to Main Menu\n")
    def handle_account_menu(self):
        """Handles commands for the account menu. Returns False if user wants to exit"""
        command = input("What would you like to do?(Enter 1-5): ")
        if command == "1" or command.lower() == "view balance":
            num = input("Please enter your account number: ")
            while not num.isdigit():
                num = input("Invalid input. Please enter your account number: ")
            num = int(num)
            acc = self.__bank.retrieve_account_int(num)
            if acc != False:
                balance = acc.balance
                print(f"Balance for account: {num}: ${balance}")
            elif acc == False:
                print("Account does not exist!")
            return True

        elif command == "2" or command.lower() == "deposit money":
            num = input("Please enter your account number: ")
            while not num.isdigit():
                num = input("Invalid input. Please enter your account number: ")
            num = int(num)
            acc = self.__bank.retrieve_account_int(num)
            if acc:
                dep = input("Please enter your account deposit amount: ")
                while not dep.isdigit():
                    dep = input("Invalid input. Please enter the deposit amount: ")
                dep = int(dep)
                truefalse = acc.deposit(dep)
                if not truefalse:
                    print("Deposit failed")
            else:
                print("Account does not exist!")
            return True

        elif command == "3" or command.lower() == "withdraw money":
            num = input("Please enter your account number: ")
            while not num.isdigit():
                num = input("Invalid input. Please enter your account number: ")
            num = int(num)
            acc = self.__bank.retrieve_account_int(num)
            if acc:
                withd = input("Please enter your account withdraw amount: ")
                while not withd.isdigit():
                    withd = input("Invalid input. Please enter the withdraw amount: ")
                withd = int(withd)
                truefalse = acc.withdraw(withd)
                if not truefalse:
                    print("Withdraw failed")
            else:
                print("Account does not exist!")
            return True

        elif command == "4" or command.lower() == "delete account":
            num = input("Please enter your account number: ")
            while not num.isdigit():
                num = input("Invalid input. Please enter your account number: ")
            num = int(num)
            acc = self.__bank.retrieve_account_int(num)
            if acc:
                self.__bank.delete_account(num)
            else:
                print("Account does not exist!")
            return True
        elif command == "5" or command.lower() == "retrieve email":
            num = input("Please enter your account number: ")
            self.__bank.retrieve_email(num)
        elif command == "6" or command.lower() == "reset password":
            num = input("Please enter your account number: ")
            password = input("Enter new account password: ")
            while len(password) < 8:
                print("Password must be at least 8 characters long!")
                password = input("Enter new account password: ")
            self.__bank.reset_password(password, num)
        elif command == "7" or command.lower() == "back to main menu" or command == "main menu":
            print("Heading back to main menu.")
            return False
        else:
            print("Invalid command!")
            return False

    def display_bank_menu(self):
        print("Welcome to bank management!\n"
              "Enter the following commands (1-5):\n"
              "1. Create New Account\n"
              "2. List All Accounts\n"
              "3. Find Account\n"
              "4. Transfer Money\n"
              "5. Back to Main Menu\n")
    def handle_bank_menu(self):
        command = input("What would you like to do?(Enter 1-5): ")
        if command == "1" or command.lower() == "create new account":
            self.__bank.add_account()
            return True
        elif command == "2" or command.lower() == "list all accounts":
            self.__bank.list_accounts()
            return True
        elif command == "3" or command.lower() == "find account":
            acc = input("Please enter your account number or account holder name: ")
            if acc.isdigit():  #if user entered account number
                acc = int(acc)
                acc = self.__bank.retrieve_account_int(acc)
                print(acc)
            else:
                acc = self.__bank.retrieve_account_str(acc)
                print(acc)
            return True
        elif command == "4" or command.lower() == "transfer money":
            amount = input("How much would you like to transfer?: ")
            while not amount.isdigit() or (amount.isdigit() and int(amount) <= 0):
                amount = input("Invalid input. How much would you like to transfer?: ")
            amount = int(amount)
            account1 = input("Please enter the number of the account you want to transfer from: ")

            account2 = input("Please enter the number of the account you want to transfer to: ")
            truefalse = self.__bank.transfer_amount(account1, account2, amount)
            if not truefalse:
                print("Transfer failed.")
            return True
        elif command == "5" or command.lower() == "back to main menu" or command == "main menu":
            print("Heading back to main menu.")
            return False
        else:
            print("Invalid command!")
            return True

    def run(self):
        self.__bank.load()
        while True:

            self.display_main_menu()
            if not self.handle_main_menu():
                self.__bank.save()
                break


if __name__ == "__main__":
    interface = Interface()
    interface.run()


