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

def filter_by_project(transactions, project_name):
    """Filters records for a specific flooring project."""
    return [t for t in transactions if project_name in t['description']]

def main():
    print("SBFO: System Initialized.")
    
    # Testing the new functions
    add_transaction("2026-04-27", "Flooring Materials", 1500.00)
    add_transaction("2026-04-28", "Hardwood installation project", 3000.00)
    
    # Calculate and print current balance
    balance = calculate_balance(transactions)
    print(f"Total Balance: ${balance}")
    
    # Save to file
    save_to_csv(transactions)
    print("Data saved to financials.csv")

if __name__ == "__main__":
    main()


