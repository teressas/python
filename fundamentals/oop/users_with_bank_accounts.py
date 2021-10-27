class BankAccount:
    # Create a BankAccount class with the attributes interest rate and balance
    accounts = []

    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)

    # Add a deposit method to the BankAccount class    
    def deposit(self, amount):
        self.account_balance += amount
        return self
        
    # Add a withdraw method to the BankAccount class
    # decreases the account balance by the given amount if there are sufficient funds; 
    # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        # check amount before taking money out
        # self.account_balance -= amount
        if self.account_balance <= amount:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        
        self.account_balance -= amount
        return self

    # Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        #print to the console: eg. "Balance: $100"
        return f"{self.account_balance}"

    # Add a yield_interest method to the BankAccount class
    # increases the account balance by the current balance * the interest rate 
    # (as long as the balance is positive)
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
        return self

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:		# here's what we have so far
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02, 1000),
            "savings" : BankAccount(.05, 3000)
        }
    
    #display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        #This calls the user and the account balance from the __init__ method
        print(f"User: {self.name}, Balance: ${self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Balance: ${self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        #have the first user transfer money to the third user and then print both users' balances
        # self.account_balance -= amount
        # user.account_balance += amount
        self.make_withdrawal(amount)
        user.make_deposit(amount)
        self.display_user_balance()
        user.display_user_balance()

adrien = User("Adrien")

adrien.account['checking'].deposit(100)
adrien.display_user_balance()