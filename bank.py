import uuid
import re
from typing import Dict, Union

from customer import Customer
from account import Account


class Bank:
    def __init__(self) -> None:
        """
        Initialize the Bank instance with an empty dictionary of customers.
        Each key is a customer ID (int), and the value is a Customer object.
        """
        self.customers: Dict[int, Customer] = {}

    def create_new_customer(self) -> None:
        """
        Prompts for a new customer's name and address, then creates the customer
        and a new account for the customer is created.
        Finally, stores the new customer in the self.customers dictionary.
        """
        unique_customer_id = self.get_unique_customer_id()
        customer_name = self.prompt_for_customer_name()
        customer_address = self.prompt_for_customer_address()

        new_customer = Customer(unique_customer_id, customer_name, customer_address)
        new_account = self.create_new_account(new_customer.customer_id)
        new_customer.add_customer_account(new_account)
        self.customers[new_customer.customer_id] = new_customer

    def create_new_account(self, customer_id: int) -> Account:
        """
        Create new account for given customer_id.

        :param customer_id: The unique ID of the customer who will own the new account.
        :return: An Account object associated with the given customer ID.
        """
        return Account(customer_id)

    def add_account_for_customer(self, customer_id: int) -> None:
        """
        Create new account for an existing customer and add it to the customer's account list.
        If the customer does not exist, print an error message.

        :param customer_id: The unique ID of the customer.
        :return: None
        """
        if customer_id in self.customers:
            customer_obj = self.customers[customer_id]
            new_account = self.create_new_account(customer_id)
            customer_obj.add_customer_account(new_account)
        else:
            print(f'Customer {customer_id} not found.')

    def find_customer(self, customer_id: int) -> Union[Customer, None]:
        """
        Find and return the Customer object for the given customer_id.
        If no matching customer is found, prints an error and returns None.

        :param customer_id: The unique ID of the customer to find.
        :return: A Customer object if found, otherwise None.
        """
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            print("Customer not found.")
            return None

    def get_unique_customer_id(self) -> int:
        """
        Generate new unique customer ID using UUID (v1).

        :return: A large integer derived from the UUID.
        """
        unique_id = uuid.uuid1()
        return unique_id.int

    def prompt_for_customer_name(self) -> str:
        """
        Prompt the user to enter a customer's name.
        Only allow letters, spaces, hyphens and apostrophes.
        Re-prompt if the inputs fails validation.

        :return: The validated and title-cased customer name.
        """
        pattern = re.compile(r"^[A-Za-z]+(?:[ '-][A-Za-z]+)*$")
        while True:
            customer_name = input("Please enter your name (letters, spaces, hyphens and apostrophes only): ").strip()
            if customer_name and pattern.fullmatch(customer_name):
                return customer_name.title()
            print("Invalid name. Please try again using only letters, spaces, hyphens and apostrophes.")

    def get_total_bank_assets(self) -> float:
        """
        Calculate the sum of all account balances in every customer's account.

        :return: The total amount of assets in the bank as a float.
        """
        total_assets = 0.0
        for customer_obj in self.customers.values():
            for account in customer_obj.customer_accounts:
                total_assets += account.balance
        return total_assets

    def prompt_for_customer_address(self) -> dict:
        """
       Prompt the user to provide address information.
       Returns a dictionary with address details or an empty dictionary if the user declines.

       :return: A dictionary containing address fields
                (street_name, street_number, city, country, and post_code),
                or an empty dictionary if the user does not wish to provide an address.
       """

        while True:
            provide_address = input("Would you like to provide and address? (y/n): ").strip().casefold()
            if provide_address in ['y', 'yes', 'yeah', 'yea']:
                while True:
                    street_name = input("Enter street name: ").strip().casefold()
                    if street_name:
                        break
                    print("Street name cannot be empty.")

                while True:
                    street_number = input("Enter street number (digits only): ").strip()
                    if street_number.isdigit():
                        street_number = int(street_number)
                        break
                    print("Please enter a valid street number (digits only).")

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
            elif provide_address in ['n', 'no', 'nope']:
                return {}
            else:
                print("Please enter 'y' or 'n'.")
