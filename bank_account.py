"""Manages individual bank accounts"""

class BankAccount:
    def __init__(self, name: str):
        self.name = name
        self.balance = 0
        self.deposits = 0
        self.withdrawals = 0

