import sqlite3
from index import User
from currentUser import CurrentUser
from savingsUser import SavingsUser
from index import display_clients

def create_tables(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                equity_card_number TEXT NOT NULL UNIQUE,
                account_type TEXT NOT NULL
            )
        ''')

def add_client(conn, user):
    with conn:
        conn.execute('''
            INSERT INTO clients (first_name, last_name, equity_card_number, account_type)
            VALUES (?, ?, ?, ?)
        ''', (user.first_name, user.last_name, user.equity_card_number, user.account_type))

def update_client(conn, equity_card_number, first_name, last_name):
    with conn:
        conn.execute('''
            UPDATE clients
            SET first_name = ?, last_name = ?
            WHERE equity_card_number = ?
        ''', (first_name, last_name, equity_card_number))

def delete_client(conn, equity_card_number):
    with conn:
        conn.execute('''
            DELETE FROM clients
            WHERE equity_card_number = ?
        ''', (equity_card_number,))

def get_client(conn, equity_card_number):
    cursor = conn.execute('''
        SELECT first_name, last_name, equity_card_number, account_type
        FROM clients
        WHERE equity_card_number = ?
    ''', (equity_card_number,))
    row = cursor.fetchone()
    if row:
        if row[3] == 'savings':
            return SavingsUser(row[0], row[1], row[2])
        elif row[3] == 'current':
            return CurrentUser(row[0], row[1], row[2])
    return None

def main():
    conn = sqlite3.connect('banking.db')
    create_tables(conn)

    while True:
        action = input("Would you like to add, update, delete a client, or perform a transaction? (a/up/del/trans/exit): ").lower()
        
        if action == 'a':
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
