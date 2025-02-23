from bank import Bank


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create new customer")
        print("2. Find customer by ID")
        print("3. Add account for existing customer")
        print("4. Show total bank assets")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bank.create_new_customer()
        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            # convert to int if needed
            try:
                customer_id = int(customer_id)
                found_customer = bank.find_customer(customer_id)
                if found_customer:
                    print(found_customer.get_customer_information())
            except ValueError:
                print("Please enter a valid integer for Customer ID.")
        elif choice == "3":
            customer_id = input("Enter customer ID to add a new account: ")
            try:
                customer_id = int(customer_id)
                bank.add_account_for_customer(customer_id)
            except ValueError:
                print("Please enter a valid integer for Customer ID.")
        elif choice == "4":
            total_assets = bank.get_total_bank_assets()
            print(f"Total bank assets: ${total_assets:.2f}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
