# Account class taken from Lab 5; has been modified a bit since Lab 5's had logical error
# id is 0

class Account:
    # Constructor
    def __init__(self, id=0, initial_balance=100, annual_interest_rate=0):
        self.__id = id
        self.__balance = initial_balance
        self.__annual_interest_rate = annual_interest_rate

    # Accessor and Mutator for id, balance, and annual interest rate
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate

    # Returns monthly interest rate
    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate / 12

    # Returns monthly interest
    def get_monthly_interest(self):
        return self.__balance * self.get_monthly_interest_rate()

    # Withdraw method
    def withdraw(self, amount):
        self.__balance -= amount

    # Deposit method
    def deposit(self, amount):
        self.__balance += amount


# Create list of 10 accounts
accounts = []
for i in range(10):
    account = Account(id=i, initial_balance=100)
    accounts.append(account)

while True:
    # Prompt user to input id
    while True:
        user_id = int(input("Enter an account id: "))
        if user_id in range(10):
            break
        else:
            print("Incorrect id!")

    # Display main menu
    while True:
        # Display menu options
        print("Main menu")
        print("1: check balance")
        print("2: withdraw")
        print("3: deposit")
        print("4: exit")

        # Prompt user to input choice
        choice = int(input("Enter a choice: "))

        # handle user's choice
        if choice == 1:
            # Display user's balance
            balance = accounts[user_id].get_balance()
            print("The balance is:", balance)
        elif choice == 2:
            # Prompt user to input withdrawal amount
            amount = float(input("Enter an amount to withdraw: "))
            # Call withdraw method
            accounts[user_id].withdraw(amount)
        elif choice == 3:
            # Prompt user to input deposit amount
            amount = float(input("Enter an amount to deposit: "))
            # Call deposit method
            accounts[user_id].deposit(amount)
        elif choice == 4:
            # exit current session
            break

    # Return to outer while loop
    continue
