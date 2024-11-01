# @USER CLASS DOCUMENTATION:

# @author: [justus kuria]

# @email: [justus.kamande@strathmore.edu]

### @overview: [The User class represents a user with an equity card, allowing them to deposit and withdraw funds. This class includes methods for initializing user details, depositing money, and withdrawing money while maintaining the user’s balance.]


#def __init__(self, first_name, last_name, equity_card_number):
#      self.first_name = first_name
#     self.last_name = last_name
#    self.equity_card_number = equity_card_number
#   self.balance = 0.0
"""
parameters
--------------
first_name: str
    The first name of the user

last_name:str
    The last name of the user 

equity_card_number: str
    The equity card number of the user

balance: float
    The balance of the user    

"""
#def deposit(self, amount):
#       self.balance += amount
#      print(f"Deposit successful! New balance: ${self.balance:.2f}")
"""
parameters
--------------  
amount: float
    The amount to be deposited
if amount deposited is 'x' it should be added to the current balance of the user

"""
#def withdraw(self, amount):
#        if amount > self.balance:
#            print("Insufficient funds!")
#        else:
#            self.balance -= amount
#            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
"""
the user is given an opportunity to withdraw cash through his equity card, 
if the amount been withdrawn is higher than the balance a insufficient funds message is outputed 
else:
     ' withdrawal succesful'
"""

# MAIN CLASS FUNCTIONS --------------------------------

## Features

- Add new clients with savings or current accounts.
"""
  if action == 'a':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            equity_card_number = input("Enter your equity card number: ")
            add_client(conn, User(first_name, last_name, equity_card_number))
            print("Client added successfully!")
"""
- Update client information.
""" 
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
"""
- Delete clients.

- Perform transactions (deposits and withdrawals) for clients.
- Store client information in an SQLite database.

# table
- table creation function
"""
def create_table(conn):
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS clients
(id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
equity_card_number TEXT NOT NULL,
balance REAL NOT NULL DEFAULT 0.0)
''')
"""
- table update function
"""
def update_table(conn):
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS clients
(id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
equity_card_number TEXT NOT NULL,
balance REAL NOT NULL DEFAULT 0.0)
''')
"""
- table delete function
"""
def delete_table(conn):
c = conn.cursor()
c.execute('''
DROP TABLE clients
''')
"""

## Usage

1. Run the `main.py` script to start the application.
   right click main.py
   select run  python file with terminal

