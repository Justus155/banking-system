import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance

    def get_account_name(self):
        return self.name

    def get_account_num(self):
        return self.account_num

    def get_balance(self):
        return self.balance

class PythonBank(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Bank")
        self.geometry("670x308")
        self.accounts = []
        self.max_accounts = 10
        self.create_user_interface()

    def create_user_interface(self):
        self.input_detail_frame = tk.LabelFrame(self, text="Input Details")
        self.input_detail_frame.place(x=16, y=16, width=208, height=250)

        self.name_label = tk.Label(self.input_detail_frame, text="Name:")
        self.name_label.place(x=8, y=32)
        self.name_entry = tk.Entry(self.input_detail_frame)
        self.name_entry.place(x=112, y=32, width=80)

        self.account_num_label = tk.Label(self.input_detail_frame, text="Account Number:")
        self.account_num_label.place(x=8, y=56)
        self.account_num_entry = tk.Entry(self.input_detail_frame)
        self.account_num_entry.place(x=112, y=56, width=80)

        self.balance_label = tk.Label(self.input_detail_frame, text="Balance:")
        self.balance_label.place(x=8, y=80)
        self.balance_entry = tk.Entry(self.input_detail_frame)
        self.balance_entry.place(x=112, y=80, width=80)

        self.deposit_label = tk.Label(self.input_detail_frame, text="Deposit:")
        self.deposit_label.place(x=8, y=104)
        self.deposit_entry = tk.Entry(self.input_detail_frame)
        self.deposit_entry.place(x=112, y=104, width=80)

        self.withdraw_label = tk.Label(self.input_detail_frame, text="Withdraw:")
        self.withdraw_label.place(x=8, y=128)
        self.withdraw_entry = tk.Entry(self.input_detail_frame)
        self.withdraw_entry.place(x=112, y=128, width=80)

        self.create_account_button = tk.Button(self.input_detail_frame, text="Create", command=self.create_account)
        self.create_account_button.place(x=112, y=152, width=80)

        self.delete_account_button = tk.Button(self.input_detail_frame, text="Delete", command=self.delete_account)
        self.delete_account_button.place(x=16, y=152, width=80)

        self.transaction_button = tk.Button(self.input_detail_frame, text="Make Transaction", command=self.make_transaction)
        self.transaction_button.place(x=16, y=180, width=176)

        self.display_button = tk.Button(self.input_detail_frame, text="Display Accounts", command=self.display_accounts)
        self.display_button.place(x=16, y=208, width=176)

        self.display_label = tk.Label(self, text="Account Details:")
        self.display_label.place(x=240, y=16)
        self.display_text = tk.Text(self, wrap=tk.WORD)
        self.display_text.place(x=240, y=48, width=402, height=184)
        self.display_text.insert(tk.END, "Welcome to Python Bank - There are currently no Accounts created")

    def create_account(self):
        name = self.name_entry.get().strip()
        account_num = self.account_num_entry.get().strip()
        balance = self.balance_entry.get().strip()

        if not name or not account_num or not balance:
            messagebox.showerror("Error", "All fields must be completed")
            return

        if len(self.accounts) >= self.max_accounts:
            messagebox.showerror("Error", "All Accounts Full!")
            return

        try:
            account_num = int(account_num)
            balance = int(balance)
        except ValueError:
            messagebox.showerror("Error", "Account Number and Balance must be integers")
            return

        new_account = Account(name, account_num, balance)
        self.accounts.append(new_account)
        self.display_text.insert(tk.END, f"\n{new_account.get_account_name()} {new_account.get_account_num()} {new_account.get_balance()}")

    def delete_account(self):
        messagebox.showinfo("Info", "Oops this isn't coded in this version!")
        self.clear_entries()

    def make_transaction(self):
        messagebox.showinfo("Info", "Transaction functionality not implemented yet!")
        self.clear_entries()

    def display_accounts(self):
        self.display_text.delete(1.0, tk.END)
        if not self.accounts:
            self.display_text.insert(tk.END, "No accounts to display")
        else:
            for account in self.accounts:
                self.display_text.insert(tk.END, f"{account.get_account_name()} {account.get_account_num()} {account.get_balance()}\n")

    