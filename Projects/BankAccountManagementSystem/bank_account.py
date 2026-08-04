"""Provide reusable bank account classes for the banking application."""
# Base Class
class BankAccount:

    bank_name = "UGA Community Bank"
    routing_number = "061100606"
    interest_rate = 0.03

    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    def display_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than $0.00.")
            print(f"Current Balance: ${self._balance:.2f}")
        else:
            self._balance += amount
            print(f"Deposited ${amount:.2f} into {self.owner}'s account.")
            print(f"New Balance: ${self._balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than $0.00")
        elif amount > self._balance:
            print("Insufficient funds.")
            print(f"Current Balance: ${self._balance:.2f}")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f} from {self.owner}'s account.")
            print(f"New Balance: ${self._balance:.2f}")

    @property
    def balance(self):
        return self._balance


# Child Classes
class SavingsAccount(BankAccount):
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self._balance += interest

        print(f"Interest Earned: ${interest:.2f}")
        print(f"New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > 1000:
            print(
                "Savings accounts cannot withdraw more than "
                "$1000.00 per transaction."
            )
        else:
            super().withdraw(amount)


class BusinessAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 10000:
            print(
                "Manager approval required for withdrawals "
                "over $10,000.00."
            )
        else:
            super().withdraw(amount)
