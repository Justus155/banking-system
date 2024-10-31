class User:
    def __init__(self, first_name, last_name, equity_card_number):
        self.first_name = first_name
        self.last_name = last_name
        self.equity_card_number = equity_card_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

def display_clients(clients):
    print("\nClient List:")
    for client in clients:
        print(f"Name: {client.first_name} {client.last_name}, Equity Card Number: {client.equity_card_number}")

