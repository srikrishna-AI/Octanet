import time
print("Welcome to Your Bank ATM")
pin = 1234
time.sleep(2)
balance =5000
User_pin = int(input("Please enter PIN number:"))
transaction_history = []
if pin != User_pin:
    print("please enter correct pin")
else:
     while True:
        print("""
        1 == balance
        2 == withdraw
        3 == deposit
        4 == change pin
        5 == transaction History
        6 == exit""")
        
        print("enter your option to further step:",end="")
        try:
            option = int(input())
        except:
            print("Invalid option")
        if option == 1:
            print(f"the current balance of Your account is:{balance}")
            transaction_history.append(f"Balace Inquiry:{balance}")
        elif option == 2:
            withdraw =int(input("enter the amont to withdraw:"))
            amount = balance - withdraw
            if amount>balance:
                print("Insuuficent balance")
            else:
                
                print(f"{withdraw} is debited to your account")
                print(f"the current balance is:{amount}")
                transaction_history.append(f"withdraw amount:{withdraw}")
        elif option == 3:
            deposit =int(input("enter the amont to deposit:"))
            balance = balance + deposit
            print(f"{deposit} is debited to your account")
            print(f"the current balance is:{balance}")
            transaction_history.append(f"Deposit Amount:{deposit}")
        elif option == 4:
            new_pin = int(input("enter the new pin:"))
            new_pin = pin
            print("your pin has changed successfully")
        elif option == 5:
            for transactions in transaction_history:
                print(transactions)
        else:
            break
         
print("Thank You for visiting Your bank")
