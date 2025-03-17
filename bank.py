import random
import string

class Bank:
    #accounts = { `account_number` : [ `name`, `account_balance`, `account_type` ] }
    accounts = {}
    
    def __init__(self, bank_name="", name="", account_balance=0.0, account_type=""):
        self.bank_name = bank_name
        self.name = name
        self.account_balance = account_balance
        self.account_type = account_type
    
    @classmethod
    def create_account(self, name, initial_deposit, account_type):
        account_balance = initial_deposit
        self.account_number = ''.join(random.choice(string.digits) for _ in range(12))
        self.accounts[self.account_number] = [name, account_balance, account_type]
        print(f"{account_type} Account was opened successfully.\n Your accounts number is {self.account_number}. Please make sure to remember it.")

    @classmethod
    def authenticate(self, name, account_number):
        #check accounts for number and name 
        for account in self.accounts:
            if account_number == account and self.accounts[account_number][0] == name:
                self.name = name
                self.account_number = account_number
                self.account_balance = self.accounts[account_number][1]
                self.account_type = self.accounts[account_number][2]
                print(f"Successfully logged in. Welcome {self.name}.")
                return name, account_number, self.account_balance, self.account_type
        else:
            print("Account does not exist.")
            return False
        
    @classmethod   
    def withdraw(self, withdraw_amount):
        #check if balance is sufficient and withdraw desired amount.
        if withdraw_amount <= self.account_balance:
            self.account_balance = self.account_balance - withdraw_amount
            print(f"Withdrew {withdraw_amount}.\nNew Balance: {self.account_balance:.2f}")
            
        else:
            print(f"Balance not sufficienct.\nCurrent Balance:{self.account_balance:.2f}")
            
    @classmethod
    def deposit(self, deposit_amount):
        #add deposit amount to balance
        self.account_balance = self.account_balance + deposit_amount
        print(f"Deposited {deposit_amount}.\nNew Balance:{self.account_balance:.2f}")
        
    
    @classmethod
    def check_balance(self, account_number):
        #find number in accounts dic and return account_balance
        for account in self.accounts:
            if account_number == account:
                print(f"Current Balance: {self.account_balance:.2f}")
    
    
    # def __str__(self):
    #     return f"{self.name}, Account Number: {self.account_number}, Balance: {self.account_balance:.2f}€" #testing
    
    
