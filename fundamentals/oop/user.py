# class User:
#     #!Construtor Function!!! Creates the instance of an object
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # take parameters of constructor function and applying those to the attributes of the instances.
#         # self is representation of instance and not the class

#     def greeting(self):
#         print(f"Hello my name is {self.first_name}!")

# adrien = User("Adrien","Dion",39)
# adrien.greeting()
    
# class User:
#     # class attributes get defined in the class 
#     bank_name = "First National Dojo"
#     # now our method has 2 parameters!
#     def __init__(self , name, email_address):
#     	# we assign them accordingly
#         self.name = name
#         self.email = email_address
#     	# the account balance is set to $0
#         self.account_balance = 0
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python

#make_withdrawal(self, amount) - 
# have this method decrease the user's balance by the amount specified

# declare a class and give it name User
# class User:		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    #make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    #display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        #This calls the user and the account balance from the __init__ method
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self,amount,user):
        #have the first user transfer money to the third user and then print both users' balances
        # self.account_balance -= amount
        # user.account_balance += amount
        self.make_withdrawal(amount)
        user.make_deposit(amount)
        self.display_user_balance()
        user.display_user_balance()

# Create 3 instances of the User class
michael = User("Mike","michael@gmail.com")
anna = User("Anna","anna@gmail.com")
nick = User("Nick","nick@gmail.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
michael.make_deposit(100)
michael.make_deposit(300)
michael.make_deposit(200)
michael.make_withdrawal(200)
michael.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
anna.make_deposit(500)
anna.make_deposit(200)
anna.make_withdrawal(200)
anna.make_withdrawal(200)
anna.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
nick.make_deposit(200)
nick.make_withdrawal(100)
nick.make_withdrawal(100)
nick.make_withdrawal(100)
nick.display_user_balance()

# BONUS: Add a transfer_money method; 
# have the first user transfer money to the third user and then print both users' balances

michael.transfer_money(200,nick)