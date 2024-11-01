import sqlite3
from index import User
from currentUser import CurrentUser
from savingsUser import SavingsUser
from index import display_clients
from mydatabase import create_tables, create_tables, add_client, update_client, delete_client, get_client

def main():
    conn = sqlite3.connect('banking.db')
    create_tables(conn)

    while True:
        action = input("Would you like to add, update, delete a client, or perform a transaction? (a/up/del/trans/exit): ").lower()
        
        if action == 'a':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            equity_card_number = input("Enter your equity card number: ")
            continue
            add_client(conn, user)
            print("Client added successfully!")

        elif action == 'up':
            equity_card_number = input("Enter the equity card number of the client to update: ")
            client = get_client(conn, equity_card_number)
            if client:
                first_name = input("Enter new first name: ")
                last_name = input("Enter new last name: ")
                update_client(conn, equity_card_number, first_name, last_name)
                print("Client updated successfully!")
            else:
                print("Client not found!")

        elif action == 'del':
            equity_card_number = input("Enter the equity card number of the client to delete: ")
            client = get_client(conn, equity_card_number)
            if client:
                delete_client(conn, equity_card_number)
                print("Client deleted successfully!")
            else:
                print("Client not found!")

        elif action == 'trans':
            equity_card_number = input("Enter the equity card number of the client: ")
            client = get_client(conn, equity_card_number)
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

    conn.close()

if __name__ == "__main__":
    main()
