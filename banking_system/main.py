from index import User
from currentUser import CurrentUser
from savingsUser import SavingsUser
from index import display_clients

def main():
    clients = []

    while True:
        action = input("Would you like to add, update, delete a client, or perform a transaction? (add/update/delete/transaction/exit): ").lower()
        
        if action == 'add':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            equity_card_number = input("Enter your equity card number: ")
            account_type = input("Enter account type (savings/current): ").lower()
            if account_type == 'savings':
                user = SavingsUser(first_name, last_name, equity_card_number)
            elif account_type == 'current':
                user = CurrentUser(first_name, last_name, equity_card_number)
            else:
                print("Invalid account type. Please enter 'savings' or 'current'.")
                continue
            clients.append(user)
            print("Client added successfully!")

        elif action == 'update':
            equity_card_number = input("Enter the equity card number of the client to update: ")
            client = next((c for c in clients if c.equity_card_number == equity_card_number), None)
            if client:
                first_name = input("Enter new first name: ")
                last_name = input("Enter new last name: ")
                client.first_name = first_name
                client.last_name = last_name
                print("Client updated successfully!")
            else:
                print("Client not found!")

        elif action == 'delete':
            equity_card_number = input("Enter the equity card number of the client to delete: ")
            client = next((c for c in clients if c.equity_card_number == equity_card_number), None)
            if client:
                clients.remove(client)
                print("Client deleted successfully!")
            else:
                print("Client not found!")

        elif action == 'transaction':
            equity_card_number = input("Enter the equity card number of the client: ")
            client = next((c for c in clients if c.equity_card_number == equity_card_number), None)
            if client:
                while True:
                    trans_action = input("Would you like to make a deposit or withdrawal? (d/w): ").lower()
                    if trans_action in ['d', 'w']:
                        try:
                            amount = float(input("Enter the amount: "))
                            if trans_action == 'd':
                                client.deposit(amount)
                            elif trans_action == 'w':
                                client.withdraw(amount)
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                    else:
                        print("Invalid option. Please enter 'd' for deposit or 'w' for withdrawal.")

                    another_action = input("Would you like to perform another transaction? (yes/no): ").lower()
                    if another_action not in ['yes', 'y']:
                        break
            else:
                print("Client not found!")

        elif action == 'exit':
            break

        else:
            print("Invalid option. Please enter 'add', 'update', 'delete', 'transaction', or 'exit'.")

    display_clients(clients)

if __name__ == "__main__":
    main()
