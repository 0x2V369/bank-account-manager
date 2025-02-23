# Bank Account Manager

A simple console-based Python application for creating and managing customers, bank accounts, and transaction data. This project demonstrates an object-oriented design that separates the core logic into four classes:

- **Bank** (manages customers and their accounts)  
- **Customer** (stores customer data, including addresses and accounts)  
- **Account** (handles deposits, withdrawals, and statements)  
- **Transaction** (records individual transactions with timestamps)

Developed by **0x2V369**.

---

## Table of Contents
1. [Overview](#overview)  
2. [Project Structure](#project-structure)  
3. [Getting Started](#getting-started)  
4. [Usage](#usage)  
5. [Possible Improvements](#possible-improvements)  
6. [License](#license)

---

## Overview

This application is designed as a **learning project** to explore Python OOP principles:

- **Create New Customer**: Prompt for name and address, automatically assign a new account.  
- **Find Customer by ID**: Retrieve and display basic customer information.  
- **Add Account**: Allow existing customers to open additional accounts.  
- **Show Total Bank Assets**: Sum the balances of all accounts in the system.  

**Note**: While the `Account` and `Transaction` classes support deposits, withdrawals, and transaction statements, the default console menu does not include direct options to perform or view these. You can easily extend `main.py` to incorporate deposit/withdraw commands or account statements.

---

## Project Structure

```
bank-account-manager/
├── main.py            # Entry point: Simple console menu to interact with the Bank
├── bank.py            # Bank class: manages customers, account creation, and assets
├── customer.py        # Customer class: holds personal info and account references
├── account.py         # Account class: deposit, withdraw, statements, etc.
└── transaction.py     # Transaction class: tracks individual transaction details
```

- **`bank.py`**  
  - Handles creating/finding customers, generating unique IDs, and calculating total assets.  
- **`customer.py`**  
  - Defines the `Customer` object, storing name, address, and multiple accounts.  
- **`account.py`**  
  - Manages account operations such as deposits, withdrawals, statements, and account types.  
- **`transaction.py`**  
  - Represents a single transaction (e.g., deposit or withdrawal) with unique ID and timestamp.  
- **`main.py`**  
  - Provides a minimal **menu** interface for user interaction with the `Bank` class.

---

## Getting Started

1. **Clone this repository** (or download the ZIP):  
   ```bash
   git clone https://github.com/0x2V369/bank-account-manager.git
   cd bank-account-manager
   ```

2. **Ensure you have Python 3.10+ installed**  
   - The project uses union-type hints (`str | None`), which require Python 3.10 or higher.

3. **(Optional) Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install any required dependencies**  
   - This project uses only the Python standard library, so no extra installation is typically needed.

---

## Usage

1. **Run the main script**  
   ```bash
   python main.py
   ```
2. **Follow the console prompts**:
   - **(1) Create New Customer**: The program will ask for name and optional address details, then create a customer record with an initial account.  
   - **(2) Find Customer by ID**: Enter a valid customer ID to retrieve that customer’s information.  
   - **(3) Add Account for Existing Customer**: Create a new account for a known customer.  
   - **(4) Show Total Bank Assets**: Summarizes the balances across all existing accounts.  
   - **(5) Exit**: Ends the program.

3. **Additional Features** (in code, not menu-driven by default):
   - **Deposit & Withdraw**: Each `Account` object has methods `deposit(amount)` and `withdraw(amount)` which create `Transaction` records. You can extend `main.py` to expose these operations in the menu.  
   - **Transaction Statements**: Each `Account` object can produce a statement via `get_statement()`, listing all transactions with timestamps.

---

## Possible Improvements

1. **Add Deposit/Withdraw to Main Menu**  
   - Currently, `deposit()` and `withdraw()` are only callable within the `Account` class. Including them in `main.py` would let you interactively update balances.

2. **List All Customers or List All Accounts**  
   - To manage many customers, a menu option to list customer IDs and details could be helpful.

3. **Display Account Statements**  
   - Expose `Account.get_statement()` in `main.py` to view transaction histories from the console.

4. **Data Persistence**  
   - The application stores data in memory. Consider saving data to a file (JSON/CSV) or a database (SQLite, PostgreSQL, etc.) for long-term usage.

5. **Advanced ID Generation**  
   - `Bank` and `Transaction` classes generate IDs by truncating UUIDs or using random numbers. Although sufficient for small-scale, you might implement a more robust or collision-resistant approach for production environments.

6. **Error Handling & Validation**  
   - Improve input validation and error handling (e.g., custom exceptions instead of `print()` statements).

7. **Concurrency & Scaling**  
   - For a larger system or multi-user scenario, consider concurrency or database locking to handle simultaneous access.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [0x2V369](https://github.com/0x2V369).

---
