# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
# This method runs when we create a new bank account
# initial_balance is how much money we start with (default is 0)
        self.account_balance = initial_balance
    def deposit(self, amount):
        #add money to the account
        self.account_balance += amount

    def withdraw(self, amount):
        #take money out of the account
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        #Show how much money is in the account
        print(f"Current Balance: ${self.account_balance}")