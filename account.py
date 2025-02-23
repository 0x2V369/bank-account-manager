import random
from transaction import Transaction


class Account:
    def __init__(self,
                 customer_id: int,
                 account_type: str | None = "Checking"
                 ) -> None:
        self.account_number = self.get_unique_account_number()
        self.balance = 0.0
        self.account_type = account_type
        self.owner = customer_id
        self.transactions = []  # Stores Transaction objects

    def deposit(self, deposit_amount) -> bool:
        """
        Add valid deposit_amount to account balance.
        """
        if not isinstance(deposit_amount, (int, float)):
            print("Deposit must be a number.")
            return False
        if deposit_amount <= 0:
            print("Deposit amount must be greater than $0.00.")
            return False

        new_transaction = Transaction(self.account_number, "deposit", deposit_amount)
        self.transactions.append(new_transaction)
        self.balance += deposit_amount
        return True

    def withdraw(self, withdraw_amount) -> bool:
        """
        Function to withdraw funds from the account.
        """
        if not isinstance(withdraw_amount, (int, float)):
            print("Withdrawal amount must be a number.")
            return False
        if withdraw_amount <= 0:
            print("Withdraw amount must be a positive value.")
            return False
        if self.balance <= 0:
            print("Your account has no funds. You can fund your account using the deposit() function.")
            return False
        if self.balance < withdraw_amount:
            print(f"There are not enough fund in your account to withdraw ${withdraw_amount}.")
            return False

        new_transaction = Transaction(self.account_number, "withdraw", withdraw_amount)
        self.transactions.append(new_transaction)
        self.balance -= withdraw_amount
        return True

    def get_balance(self) -> float:
        """
        Prints account balance.
        """
        return self.balance

    def get_statement(self) -> str:
        """
        Returns a formatted account statement listing all transactions.
        If there are no transactions, returns a message indicating that.
        """
        if not self.transactions:
            return f"Account {self.account_number} has no transactions."

        statement_lines = [f"Account Statement for Account {self.account_number}"]
        for transaction in self.transactions:
            # Format each transaction's details.
            # Note: Adjust the formatting as needed depending on the attributes you want to show.
            line = (
                f"Transaction Type: {transaction.transaction_type.capitalize()}, "
                f"Amount: ${transaction.tx_amount:.2f}, "
                f"Date: {transaction.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            statement_lines.append(line)

        return "\n".join(statement_lines)

    def get_unique_account_number(self) -> str:
        """
        Generates a random 10-digit number and returns it as a string.
        Note: this needs to be improved if the project is scaled.
        """
        return str(random.randint(1000000000, 9999999999))

    def rename_account(self, new_account_type) -> None:
        """
        Rename the account.
        """
        self.account_type = new_account_type
