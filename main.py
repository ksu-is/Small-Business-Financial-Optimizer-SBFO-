# Small Business Financial Optimizer (SBFO)
# Author: Leonel Zepeda
# Purpose: Track weekly financials, transactions, and project spending.

# Initialize a list to store transaction dictionaries
transactions = []

def add_transaction(date, description, amount):
    """Adds a new financial transaction to the records."""
    entry = {"date": date, "description": description, "amount": amount}
    transactions.append(entry)
    print(f"Added: {description} for ${amount}")

def main():
    print("SBFO: System Initialized.")
    # Example usage:
    add_transaction("2026-04-27", "Flooring Materials", 1500.00)
    print(f"Current transactions: {len(transactions)}")

if __name__ == "__main__":
    main()
