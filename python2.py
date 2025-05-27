class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):   
        if self.balance < amount
            print("Insufficient funds")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance

def default_test():
    account = Account(account_number="12345678", balance=1000)
    print(account.account_number)
    print(account.balance)