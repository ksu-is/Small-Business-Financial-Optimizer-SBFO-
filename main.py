# Small Business Financial Optimizer (SBFO)
# Author: Leonel Zepeda
# Purpose: Track weekly financials, transactions, and project spending.

import csv # Import goes at the very top

# Initialize a list to store transaction dictionaries
transactions = []

def add_transaction(date, description, amount):
    """Adds a new financial transaction to the records."""
    entry = {"date": date, "description": description, "amount": amount}
    transactions.append(entry)
    print(f"Added: {description} for ${amount}")

def add_invoice(invoice_number, client, amount):
    """Adds a new invoice to track accounts receivable."""
    entry = {"invoice": invoice_number, "client": client, "amount": amount}
    # (Append logic here)
    print(f"Logged invoice #{invoice_number} for {client}")

def calculate_balance(transactions):
    """Calculates total net balance."""
    total = sum(item['amount'] for item in transactions)
    return total

def save_to_csv(data):
    """Saves transaction list to a local CSV file."""
    with open('financials.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "description", "amount"])
        writer.writeheader()
        writer.writerows(data)

def main():
    print("SBFO: System Initialized.")
    # Example usage:
    add_transaction("2026-04-27", "Flooring Materials", 1500.00)
    print(f"Current transactions: {len(transactions)}")

if __name__ == "__main__":
    main()


