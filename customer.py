class Customer:
    def __init__(self, unique_customer_id, customer_name, customer_address=""):
        self.customer_id = unique_customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_accounts = []  # list of customer account ids

    def get_customer_information(self):
        pass

    def update_customer_detaisl(self):
        pass

    def add_customer_account(self):
        pass
