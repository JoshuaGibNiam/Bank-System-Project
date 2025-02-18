# Bank System Project

This is a program simulating a bank system, with all the basic features of a normal bank included.

---
## Functions
1. **Create bank account**: Create a bank account with the account holder name,
account number, and balance.
2. **Deposit**: Deposit a certain amount to an account. Automatically rejects invalid 
amounts.
3. **Withdraw**: Withdraw a certain amount from an account. Automatically rejects 
invalid amounts, and stop process if the account  has insufficient funds.
4. **Transfer amount**: Transfer a certain amount from an account to another account. 
Automatically rejects invalid amounts or stop process if the account has insufficient funds.
5. **Delete account**: Delete an account by account number.
6. **List accounts**: List all the active accounts: account number -> account holder
7. **View balance**: View your balance by giving your account number
8. **Find account**: Find your account by your account number OR account holder.
9. **Logging**: Automatically logs all accounts to a file, so that the data can be 
loaded again the next time you use the program.

---
## Usage
1. When you run the program (main menu), it will ask you whether you want to manage 
the bank or manage accounts. Enter a number (1-3) to state your command.
2. Account management includes:
    - View balance
    - Deposit money
    - Withdraw money
    - Delete account
    - Back to main menu
Enter a number (1-5) to state your command. 
3. Bank management includes:
    - Create a new account
    - List all accounts
    - Find account
    - Transfer money
    - Back to main menu
Enter a number (1-5) to state your command.
4. To end the program, go back to main menu and enter 3 (exit) to save changes made
to the bank and allow for a graceful exit.
---
## Code
1. This program consists of 4 files of code:
    1. bank_account.py: BankAccount class, which manages individual bank accounts.
    2. bank.py: Bank class, which manages the bank as a whole.
    3. interface.py: Front-end of the program, provides menu navigation and handles
       user inputs.
    4. main.py: Where the program will be run directly.

---
Monday, 18th of February 2025, 5:51 p.m.

