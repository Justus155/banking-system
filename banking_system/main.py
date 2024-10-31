from index import User
from index import display_clients
def main():
    clients = []

    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        equity_card_number = input("Enter your equity card number: ")

        user = User(first_name, last_name, equity_card_number)
        clients.append(user)

        while True:
            action = input("Would you like to make a deposit or withdrawal? (d/w): ").lower()
            if action in ['d', 'w']:
                try:
                    amount = float(input("Enter the amount: "))
                    if action == 'd':
                        user.deposit(amount)
                    elif action == 'w':
                        user.withdraw(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            else:
                print("Invalid option. Please enter 'd' for deposit or 'w' for withdrawal.")

            another_action = input("Would you like to perform another transaction? (yes/no): ").lower()
            if another_action not in ['yes', 'y']:
                break

        another_client = input("Would you like to add another client? (yes/no): ").lower()
        if another_client not in ['yes', 'y']:
            break

    display_clients(clients)

if __name__ == "__main__":
    main()
