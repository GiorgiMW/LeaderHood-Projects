profile = {}

#1. creating an account for bank
def create_account():
    account_num = input("Enter account number: ")
    name = input("Enter holder's name: ")
    deposit = int(input("Enter deposit amount: "))
    profile[account_num] = {"Name": name, "Balance": deposit}
    print("Account created succesfully")

#2. Performing a transaction
def transaction():
    account_num = input("Enter account number: ")
    if account_num in profile:
        transactions = input("Enter 'd' for deposit, 'w' for withdraw: ")
        amount = int(input("Enter amount: "))
        if transactions == "d":
            profile[account_num]["Balance"] += amount
            print(f"Deposited {amount}. New balance is {profile[account_num]["Balance"]}")
        elif transactions == "w":
            if amount > profile[account_num]["Balance"]:
                print("Insufficient funds")
            else:
                profile[account_num]["Balance"] -= amount
                print(f"Withdraw {amount}. New balance is {profile[account_num]["Balance"]}")
        else:
            print("Incorrect type of transaction")
    else:
        print("Account not found")

#3 working for update user's account info
def update_account_info():
    account_num = input("Enter account number: ")
    if account_num in profile:
        name = input("Enter new account holder's name: ")
        profile[account_num]["Name"] = name
        print("Account info updated succesfully")
    else:
        print("Account not found")

#4 creating function for account delete
def delete_account():
    account_num = input("Enter account number: ")
    if account_num in profile:
        del profile[account_num]
        print("Account deleted succesfully")
    else:
        print("Account not found")

#5 creating a function for searching user's account info
def search_account_info():
    account_num = input("Ente account number: ")
    if account_num in profile:
        print(f"Account Number: {account_num}")
        print(f"Account Holder: {profile[account_num]["Name"]}")
        print(f"Balance: {profile[account_num]["Balance"]}")
    else:
        print("Account not found")

#6 creating a fucntion for view customer's lists
def view_customer_list():
    if profile:
        for account_num, info in profile.items():
            print(f"Account Number: {account_num}")
            print(f"Account Holder: {info["Name"]}")
            print(f"Balance: {info["Balance"]}")
    else:
        print("No account found")

#7 creating exiting system
def system_exit():
    print("Exiting system...")
    exit()

#8 working on bank main system 
def system_main():
    while True:
        print("1. Create Account")
        print("2. Perform transaction")
        print("3. Update Account Info")
        print("4. Delete Account")
        print("5. Search Account Info")
        print("6. View Customer's List")
        print("7. Exit system")
        users_choice = input("Enter your command(number): ")
        if users_choice == "1":
            create_account()
        if users_choice == "2":
            transaction()
        if users_choice == "3":
            update_account_info()
        if users_choice == "4":
            delete_account()
        if users_choice == "5":
            search_account_info()
        if users_choice == "6":
            view_customer_list()
        if users_choice =="7":
            system_exit()

system_main()
