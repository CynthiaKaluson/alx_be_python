# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Create a bank account starting with $100
    account = BankAccount(100)

    # Check if user gave us a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command (like "deposit:50") into parts
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Do what the user asked for
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")  # Fixed the capitalization
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

# THIS LINE SHOULD BE AT THE LEFT MARGIN (NO INDENTATION)
if __name__ == "__main__":
    main()