# Small Business Financial Optimizer (SBFO)
# Final Version - Sprint 3 Completion
# Author: Leonel Zepeda

import csv
import os

# Global variable to store financial data
transactions = []
FILENAME = 'financials.csv'

def load_from_csv():
    """Reads financial records from the CSV file if it exists."""
    global transactions
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as f:
                reader = csv.DictReader(f)
                transactions = list(reader)
                # Convert string amounts back to floats for math
                for t in transactions:
                    t['amount'] = float(t['amount'])
            print(f"--- System: {len(transactions)} records loaded successfully. ---")
        except Exception as e:
            print(f"Error loading file: {e}")
    else:
        print("--- System: No existing records found. Starting fresh. ---")

def save_to_csv():
    """Saves the current transaction list to the CSV file."""
    try:
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["date", "description", "amount"])
            writer.writeheader()
            writer.writerows(transactions)
        print("--- System: Data saved to disk. ---")
    except Exception as e:
        print(f"Error saving data: {e}")

def add_transaction():
    """Collects user input and adds a transaction with error handling."""
    date = input("Enter date (YYYY-MM-DD): ")
    desc = input("Enter description (e.g., Flooring Materials - Job #101): ")
    
    try:
        amount = float(input("Enter amount (use negative for expenses): "))
        entry = {"date": date, "description": desc, "amount": amount}
        transactions.append(entry)
        print(f"Successfully added: {desc}")
    except ValueError:
        print("Invalid amount! Please enter a number (e.g., 1500.50).")

def show_summary():
    """Calculates and displays the current financial position."""
    if not transactions:
        print("No transactions recorded yet.")
        return

    total_balance = sum(t['amount'] for t in transactions)
    print("\n" + "="*30)
    print(f"CURRENT BALANCE: ${total_balance:,.2f}")
    print("="*30)
    for t in transactions:
        print(f"{t['date']} | {t['description'][:20]:<20} | ${t['amount']:>10,.2f}")
    print("="*30)

def main():
    """Primary Program Flow."""
    print("Welcome to the Small Business Financial Optimizer")
    load_from_csv()
    
    while True:
        print("\n[1] Add Transaction/Invoice")
        print("[2] View Financial Summary")
        print("[3] Save and Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            save_to_csv()
            print("Goodbye, Leonel!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()

