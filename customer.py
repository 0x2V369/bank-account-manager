from typing import Dict, List, Any
from account import Account


class Customer:
    def __init__(self, unique_customer_id: int,
                 customer_name: str,
                 customer_address: dict,
                 ) -> None:
        """
        Initialize a Customer object with an ID, name, and optional address.

        :param unique_customer_id: The unique integer ID for the customer.
        :param customer_name: The customer's name.
        :param customer_address: A dictionary containing address fields, if provided.
        """
        self.customer_id: int = unique_customer_id
        self.customer_name: str = customer_name
        self.customer_address: dict = customer_address if customer_address is not None else {}
        self.customer_accounts: List[Account] = []

    def get_customer_information(self) -> Dict[str, Any]:
        """
        Return Customer information as a dictionary.
        """
        info = {
            "Customer ID": self.customer_id,
            "Customer Name": self.customer_name,
        }
        if self.customer_address:
            info['Customer Address'] = self.customer_address
        return info

    def update_customer_details(self,
                                new_name: str | None = None,
                                new_address: dict | None = None) -> None:
        """
        Update customer details.

        :param new_name: The new name for the customer.
        :param new_address: A dictionary representing the new address data.
        :return: None
        """
        if new_name:
            self.customer_name = new_name
        if new_address:
            self.customer_address = new_address


    def add_customer_account(self, new_account: Account) -> None:
        """
        Add a new account to this customer's account list.

        :return: None
        """
        self.customer_accounts.append(new_account)
