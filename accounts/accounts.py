class account:
    def __init__(self):
        self.accountname = "empty"
        self.accountnum = 0
        self.balance = 0

    #deposit
    def deposit(self, amt):
        self.balance += amt
    #withdrawal
    def withdraw(self,amt):
        self.balance-=amt
        