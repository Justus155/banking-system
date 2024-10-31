from index import User
class SavingsUser(User):
    def deposit(self, amount):
        new_balance = self.get_balance() + amount
        self.set_balance(new_balance)
        print(f"Deposit successful! New balance: ${new_balance:.2f}")

    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Insufficient funds!")
        else:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Withdrawal successful! New balance: ${new_balance:.2f}")
