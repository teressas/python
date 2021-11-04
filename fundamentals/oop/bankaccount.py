class BankAccount:
    # Create a BankAccount class with the attributes interest rate and balance
    accounts = []

    def __init__(self, account_balance, int_rate):
        self.account_type = type
        self.account_balance = 0
        self.int_rate = 0.01
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
        return self

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

# Create 2 accounts
savings = BankAccount("savings")
checking = BankAccount("checking")

# To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
savings.deposit(200).deposit(100).deposit(200).withdraw(200).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all 
# in one line of code (i.e. chaining)
checking.deposit(1000).deposit(130).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()

BankAccount.print_all_accounts()