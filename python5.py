class SavingsAccount:
    def __init__(self,account_number,balance,interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        interset = self.balance*(self.interest_rate/100)
        return interset
    
    def apply_interest(self):
        self.balance = self.balance + self.balance*(self.interest_rate/100)
        
def default_test():
    account = SavingsAccount(account_number="12345678", balance=1000.0, interest_rate=5.0)
    print(account.account_number)
    print(account.balance)
    print(account.interest_rate)
    interest = account.calculate_interest()
    print(interest)
    account.apply_interest()
    print(account.balance)