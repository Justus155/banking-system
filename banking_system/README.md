#USER CLASS DOCUMENTATION:

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

#main class
