from customer import Customer
from account import Account
import uuid


class Bank:
    def __init__(self):
        self.customers = {
        }
        self.transactions = []

    def create_new_customer(self):
        """
        Create New customer
        :return: Add new customer to banks customer ledger
        """
        unique_customer_id = self.generate_unique_customer_id()
        customer_name = self.get_customer_name()
        customer_address = self.add_customer_address()

        new_customer = Customer(unique_customer_id, customer_name, customer_address)
        new_account = self.create_new_account(new_customer.customer_id)
        new_customer.customer_accounts.append(new_account.account_number)
        self.customers[new_customer.customer_id] = {
            'customer': new_customer,
            'account': new_account,
        }

    def create_new_account(self, customer_id):
        """
        Create new account for given customer_id
        :param customer_id:
        :return: new Account()
        """
        return Account(customer_id)

    def find_customer(self, customer_id="", account_number=""):
        """Find customer by the id or account_number"""
        pass

    def generate_unique_customer_id(self):
        """
        Generate new unique customer id
        :return: uuid
        """
        unique_id = uuid.uuid1()
        return unique_id.int

    def get_customer_name(self):
        """
        Get customer name
        :return: customer_name
        """
        while True:
            customer_name = input("Please enter your name: ").strip()
            if customer_name.replace(" ", "").isalpha():
                return customer_name
            print("Customer name cannot be empty or contain digits. Please enter a valid name.")

    def get_total_bank_assets(self):
        """Function returns sum of all assets that are deposited in the bank"""
        total_assets = 0

        for customer_info in self.customers.values():
            for account in customer_info["account"]:
                total_assets += account.get_balance()

        return total_assets

    def add_customer_address(self):
        """
        Get address from customer as a dictionary
        :return: empty dictionary or structured address
        """

        street_name = ""
        street_number = ""
        city = ""
        country = ""
        post_code = ""

        while True:
            give_address = input("Would you like to provide an address (y/n)?: ").strip().casefold()
            if give_address in ['yes', 'yea', 'y', 'yeah']:
                print("Please provide your address.")
                street_name = input("Please provide street name: ").strip().title()
                street_number = input("Please provide street number: ").strip()
                city = input("Please provide name of the city: ").strip().title()
                country = input("Please provide name of the country: ").strip().title()
                post_code = input("Please provide postcode: ").strip().upper()
                return {
                    "street_name": street_name,
                    "street_number": street_number,
                    "city": city,
                    "country": country,
                    "post_code": post_code
                }
            else:
                return dict()
