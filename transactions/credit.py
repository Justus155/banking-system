
from accounts import accounts


class credit(accounts/accounts):
    def __init__(self,name="empty",num=0,amt=0,credit=100):
        super().__init__()
        self.accountname=name
        self.accountnum=num
        self.balance=amt
        self.creditlimit=1000

    #methods
    def set_creditlimit(self, num):
        self.creditlimit=num

    def get_creditlimit(self):
        return self.creditlimit
    def print_account(self):
        print(f"{self.accountname}{self.accountnum}{self.balance}{self.creditlimit}")
