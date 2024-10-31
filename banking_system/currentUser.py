from index import User
class CurrentUser(User):
    def __init__(self, username, password, balance=0):
        super().__init__(username, password, balance)
    def deposit(self, amount):
        new_balance = self.get_balance() + amount
        self.set_balance(new_balance)
        print(f"Deposit successful! New balance: ${new_balance:.2f}")

    def withdraw(self, amount):
        # CurrentUser allows overdraft up to $100
        if amount > self.get_balance() + 100:
            print("Insufficient funds!")
        else:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Withdrawal successful! New balance: ${new_balance:.2f}")
