
from index import User


def main(index):

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    equity_card_number = input("Enter your equity card number: ")

    user = User(first_name, last_name, equity_card_number)

    while True:
        action = input("Would you like to make a deposit or withdrawal? (d/w): ").lower()
        if action in ['d', 'w']:
            amount = float(input("Enter the amount: "))
            if action == 'd':
                user.deposit(amount)
            elif action == 'w':
                user.withdraw(amount)
        else:
            print("Invalid option. Please enter 'd' for deposit or 'w' for withdrawal.")

        another_action = input("Would you like to perform another transaction? (yes/no): ").lower()
        if another_action != 'yes':
            break

if __name__ == "__main__":
    main()
