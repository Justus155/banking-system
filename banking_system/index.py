from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, first_name, last_name, equity_card_number):
        self.first_name = first_name
        self.last_name = last_name
        self.equity_card_number = equity_card_number
        self.account_type = None
        self.__balance = 0.0  # Private attribute

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

def display_clients(clients):
    print("\nClient List:")
    for client in clients:
        print(f"Name: {client.first_name} {client.last_name}, Equity Card Number: {client.equity_card_number}, Balance: ${client.get_balance():.2f}")
