from datetime import datetime
import uuid


class Transaction:
    def __init__(self,
                 account_number: str,
                 transaction_type: str,
                 amount: float
                 ) -> None:
        self.transaction_id = self.get_new_transaction_id()  # str
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

    def get_transaction_details(self) -> dict:
        """
        :return transaction_details: Return the transaction details dictionary.
        """
        return self.transaction_details

    def get_new_transaction_id(self) -> str:
        """
        Generate unique transaction id.

        :return str: Transaction ID string consisting of 10 integers
        """
        tx_id = str(uuid.uuid1().int)
        return tx_id[:10]
