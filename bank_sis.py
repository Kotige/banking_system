menu = """
[d] Deposit
[w] Withdraw
[s] Bank statement
[q] Quit
"""

balance =  0
withdraw_limit_value = 500
bank_statement = " "
withdraw_number = 0
WITHDRAW_LIMIT_NUMBER = 3

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Enter the deposit amount: "))

        if value > 0:
            balance += value
            bank_statement += f"Deposit: R$ {value:.2f}\n"
        
        else:
            print("Operation failed. Entered value is not valid.")
    
    elif option == "w":
        value = float(input("Inform the withdrawal amount: "))

        exceeded_balance = value > balance

        exceeded_limit = value > withdraw_limit_value

        exceeded_number = withdraw_number >= WITHDRAW_LIMIT_NUMBER

        if exceeded_balance: 
            print("Insufficient funds.")

        elif exceeded_limit:
            print("Withdrawal amount exceeded limit.")
        
        elif exceeded_number:
            print("Maximum number of withdrawals exceeded the limit.")

        elif value > 0:
            balance -= value
            bank_statement += f"Withdraw: R$ {value:.2f}\n"
            withdraw_number += 1
        
        else: 
            print("Operation faild. Try again.")
    
    elif option == "s":
        print("\n=================== Bank Statement ===================")
        print("No bank transactions were carried out." if not bank_statement else bank_statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("========================================================")
    
    elif option == "q":
        break

    else:
        print('Invalid operation, please reselect the desired operation.')