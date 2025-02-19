from account import Account


class Customer:
    def __init__(self, unique_customer_id, customer_name, customer_address=""):
        self.customer_id = unique_customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_accounts = []  # list of customer account ids

    def get_customer_information(self):
        """Return Customer information"""
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")


    def update_customer_details(self):
        pass

    def add_customer_account(self):
        """Create and add new account"""
        new_account = Account(self.customer_id)
        self.customer_accounts.append(new_account.account_number)
