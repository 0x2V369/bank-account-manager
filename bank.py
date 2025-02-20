from customer import Customer
from account import Account
import uuid
import re


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
        # Store accounts in a list for each customer
        self.customers[new_customer.customer_id] = {
            'customer': new_customer,
            'accounts': [new_account],
        }

    def create_new_account(self, customer_id):
        """
        Create new account for given customer_id
        """
        return Account(customer_id)

    def add_account_for_customer(self, customer_id):
        """Create a new account for an existing customer"""
        new_account = self.create_new_account(customer_id)
        if customer_id in self.customers:
            self.customers[customer_id]['accounts'].append(new_account)
        else:
            print(f"Customer {customer_id} not found.")

    def find_customer(self, customer_id=""):
        """Find and return the customer and their account information for the given customer_id."""
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            print("Customer not found.")
            return None

    def generate_unique_customer_id(self):
        """
        Generate new unique customer id.
        """
        unique_id = uuid.uuid1()
        return unique_id.int

    def get_customer_name(self):
        """
        Prompt the user to enter a customer's name.
        Only allow letters, spaces, hyphens and apostrophes.
        """
        pattern = re.compile(r"^[A-Za-z]+(?:[ '-][A-Za-z]+)*$")
        while True:
            customer_name = input("Please enter your name (letters, spaces, hyphens and apostrophes only): ").strip()
            if customer_name and pattern.fullmatch(customer_name):
                return customer_name.title()
            print("Invalid name. Please try again using only letters, spaces, hyphens and apostrophes.")

    def get_total_bank_assets(self):
        """Function returns sum of all assets that are deposited in the bank"""
        total_assets = 0
        for customer_info in self.customers.values():
            for account in customer_info['accounts']:
                total_assets += account.balance
        return total_assets


    def add_customer_address(self):
        """
        Prompt the user to provide address information.
        Returns a dictionary with address details or and empty dictionary if user declines.
        """
        while True:
            provide_address = input("Would you like to provide and address? (y/n): ").strip().casefold()
            if provide_address in ['y', 'yes', 'yeah', 'yea']:
                break
            elif provide_address in ['n', 'no', 'nope']:
                return {}
            else:
                print("Please enter 'y' or 'n'.")

        # Prompt for address details
        while True:
            street_name = input("Enter stree name: ").strip().casefold()
            if street_name:
                break
            print("Street name cannot be empty.")

        while True:
            street_number = input("Enter street number (digits only): ").strip()
            if street_number.isdigit():
                street_number = int(street_number)
                break
            print("PLease enter a valid street number (digits only).")

        while True:
            city = input("Enter city: ").strip().casefold()
            if city:
                break
            print("City cannot be empty.")

        while True:
            country = input("Enter country: ").strip().casefold()
            if country:
                break
            print("Country cannot be empty.")

        while True:
            postal_code = input("Enter postal code: ").strip().casefold()
            if postal_code:
                break
            print("Postal code cannot be empty.")

        return {
            "street_name": street_name,
            "street_number": street_number,
            "city": city,
            "country": country,
            "post_code": postal_code,
        }
