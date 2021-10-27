class BankAccount:
    # Create a BankAccount class with the attributes interest rate and balance
    accounts = []

    def __init__(self, account_balance, int_rate):
        self.account_type = type
        self.account_balance = account_balance
        self.int_rate = int_rate
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
        print(f"Balance: ${self.account_balance}")
        # return(f"{self.account_balance}")

    # Add a yield_interest method to the BankAccount class
    # increases the account balance by the current balance * the interest rate 
    # (as long as the balance is positive)
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# user class
class User:		# here's what we have so far
    def __init__(self, name):
        self.name = name
        # self.account_balance = 0
        self.accounts = {
            "checking": BankAccount(1000, 0.02),
            "savings": BankAccount(1000, 0.02)
        }
    
        #self.accounts = BankAccount(1000,0.02)
    
    # adding the deposit method
    def make_deposit(self, amount, type):	# takes an argument that is the amount of the deposit
        self.accounts[type].deposit(amount)	# the specific user's account increases by the amount of the value received
        return self

    #make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount, type):
        self.accounts[type].withdraw(amount)
        return self

    #display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        #This calls the user and the account balance from the __init__ method
        print(f"User: {self.name}, Checking Balance: {self.accounts['checking'].account_balance}")
        print(f"User: {self.name}, Savings Balance: {self.accounts['savings'].account_balance}")
        return self

    def transfer_money(self,amount,user):
        #have the first user transfer money to the third user and then print both users' balances
        # self.account_balance -= amount
        # user.account_balance += amount
        self.make_withdrawal(amount)
        user.make_deposit(amount)
        self.display_user_balance()
        user.display_user_balance()

teressa = User("teressa")
teressa.make_deposit(100,"checking")
teressa.make_deposit(100,"savings")
teressa.display_user_balance()