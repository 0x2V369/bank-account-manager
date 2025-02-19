import random
from transaction import Transaction


class Account:
    def __init__(self, customer_id):
        self.account_number = self.get_unique_account_number()
        self.balance = 0
        self.account_type = "Checking"
        self.owner = customer_id
        self.transactions = []

    def deposit(self, deposit_amount):
        """Add valid deposit_amount to account balance."""

        if deposit_amount <= 0:
            print("Deposit amount must be greater that $0.00.")
            return

        new_transaction = Transaction(self.account_number, "deposit", deposit_amount)
        self.transactions.append(new_transaction.transaction_id)
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):

        # TODO check withdraw amount > 0
        # TODO check that the account has enough funds to withdraw
        # TODO add to customer report that this amount was withdrawn
        # Check if there is any fund in the account
        if withdraw_amount <= 0:
            print("Withdraw amount must be a positive value.")
        elif not self.balance > 0:
            print("Your account has no funds.")
            print("You can fund your account using the deposit() function.")
        elif self.balance < withdraw_amount:
            print(f"There is not enough funds in your account to make a withdraw of ${withdraw_amount}")

        new_transaction = Transaction(self.account_number, "withdraw", withdraw_amount)
        self.transactions = new_transaction
        self.balance -= withdraw_amount

    def get_balance(self):
        """Prints account balance"""
        return print(f"Current balance for account:{self.account_number} is ${self.balance}.")

    def get_statement(self):
        # TODO get account statement
        pass

    def get_unique_account_number(self):
        """Generates a random 10-digit number and returns it as a string"""
        return str(random.randint(1000000000, 9999999999))

    def rename_account(self, new_account_type):
        """Rename the account"""
        self.account_type = new_account_type
