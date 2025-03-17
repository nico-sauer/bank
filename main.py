from bank import Bank
import time
import sys



def main():
    while True:
        bank_name = "The Bank"
        print("***********************************")
        print("*              ***                *")
        print(f"*       Welcome to {bank_name}       *")
        print("*         Online Banking          *")
        print("*              ***                *")
        print("***********************************")
        print("")
        print(" >>> Please choose 1 to log into existing account\nor 2 to open a new account.\nEnter 'x' to quit:")
    
        option = input("—> ").lower()
        
        while option not in (["1", "2", "x"]):
            print("Invalid. Try again.")
            option = input("—> ").lower()
        
        if option == "1":
            print("To log in please enter your name and account number.")
            name = input("Name: ")
            account_number = input("Account Number: ")
            
            user = Bank.authenticate(name, account_number)
            if user:
                time.sleep(3)
                print(f"Welcome to {bank_name}")
                bank_menu(account_number)
                break
            time.sleep(2)
                
                                       
        elif option == "2":
            account = new_customer(bank_name)
            account.create_account(account.name, account.account_balance, account.account_type)
            #print(account)
            time.sleep(2)
        
        else:
            sys.exit()
            
    
    
#registration if option 1
def new_customer(bank_name):
    
    
    name = input("Name: ")

    option = input("Choose 1 to open Checking Account. Choose 2 to open Savings Account:\n—> ")

    while option not in (["1", "2"]):
        print("Invalid. Try again.")
        option = input("—> ")
    
    if option == "1":
        account_type = "Checking"
        
    else:
        account_type = "Savings"
    
    initial_deposit = float(input("Initial Deposit: "))
    
        
    return Bank(bank_name, name, initial_deposit, account_type)
    
#bank account menu if option 2 successful
         
def bank_menu(account_number):
   
    while True:
        print("")
        print("")
        print("")
        print("************************")
        print(" >>> Menu Options:")
        print("  > 1. Withdrawal.")
        print("  > 2. Deposit.")
        print("  > 3. Check balance.")
        print("************************")


        option = input("Enter your option (1 to 3) or 'x' to quit:\n—> ").lower()
        
        while option not in (["1", "2", "3", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 to 3 or 'x' to quit):\n—> ").lower()
        
        if option == "1":
            withdraw_amount = float(input("Enter Withdrawal Amount:\n—>"))
            Bank.withdraw(withdraw_amount)
            time.sleep(2)
            
            
        elif option == "2":
            deposit_amount = float(input("Enter Deposit Amount:\n—>"))
            Bank.deposit(deposit_amount)
            time.sleep(2)
        
        elif option == "3":
            Bank.check_balance(account_number)
            time.sleep(2)
            
            
        elif option == "x":
            sys.exit() 

       

    


if __name__ == "__main__":
    main()

