from datetime import datetime


class Transaction:
    def __init__(self, account_number, transaction_type, amount):
        self.transaction_id = 0
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.utcnow()

    def get_transaction_details(self, transaction_id):
        pass
