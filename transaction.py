from datetime import datetime


class Transaction:
    def __init__(self, account_number, transaction_type, amount):
        self.transaction_id = 0
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.tx_amount = amount
        self.timestamp = datetime.utcnow()
        self.transaction_details = {
            "tx_id": self.transaction_id,
            "account_number": self.account_number,
            "tx_type": self.transaction_type,
            "tx_amount": self.tx_amount,
            "tx_timestamp": self.timestamp,
        }

    def get_transaction_details(self, transaction_id):
        pass