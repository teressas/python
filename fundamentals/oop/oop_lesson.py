# OOP
# object oriented programming

# attributes: everything that makes up object
# method: things the can be performed

def function_name():
    pass

class House:
# class names eg. FunctionName
    #belongs to each instance of the class
    blueprint_creator = "Tyler Tbo"
    #method
    def __init__(self, door_count:int, is_front_door_open=False, is_front_door_lock=True):
        # self - instance of the object
        self.owner = owner
        self.door_count = door_count
        self.is_front_door_open = is_front_door_open
        self.is_front_door_lock = is_front_door_lock
    
    def info(self):
        #total length will be 80, subtracts house infor from 80
        # print(f"{' House Info ':*^80}")
        print(f"blueprint creator: {House.blueprint_creator}")
        print(f"owner:{self.owner}")
        print(f"door_count:{self.door_count}")
        print(f"is_front_door_open: {self.is_front_door_open}")
        print(f"is_front_door_lock: {self.is_front_door_lock}")
        return "yeah!"

    def open_front_door(self):
        if not self.is_front_door_lock:
            self.is_front_door_open = True
        else:
            print("door is locked")

    def close_front_door(self):
        self.is_front_door_open = False

    # acts on an instance of the object -> i.e self
    def unlock_f_door(self):
        self.is_front_door_lock = False
        return self
    
    # acts on a class -> ie: cls, get house class passed in
    @classmethod
    def change_blueprint_creator (cls,name):
        cls.blueprint_creator = name

    # acts on nothing, no self, no cls, not related to class
    # class, attribute: dob; staticmethod calculates age. 
    @staticmethod
    #validate input going into class
    def valid_house():

tylerHouse = House("Tyler", 3, is_front_door_open=True)
blairsHouse = House("Blair", 50)

print(tylerHouse.is_front_door_open)
print(blairsHouse.is_front_door_open)
# returns in terminal: "bound method User.make_withdrawal of <__main__.User object at 0x100f3fb50>>"
# printing out the place in memory

tylerHouse.info()
House.change_blueprint_owner("Jake Duncan")
tylerHouse.open_front_door()
tylerHouse.info()
blairsHouse.info()

# class method

class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum



