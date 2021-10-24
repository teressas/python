#example: my_new_favorite_language = 'Python' # variable declaration, initialize string
#variable declaration
num1 = 42 

#variable declaration
num2 = 2.3 

#variable declaration
boolean = True 

#variable declaration, initialize string
string = 'Hello World' 

#variable declaration, composite-list-initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 

#variable declaration, composite-dictionary-initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#variable declaration, composite-Tuples-initialize
fruit = ('blueberry', 'strawberry', 'banana')

#log statement, type check
print(type(fruit))

#log statement, composite-list-access value
print(pizza_toppings[1])

#composite-list-add value
pizza_toppings.append('Mushrooms')

#log statement, composite-dictionary-access value
print(person['name'])

#variable declaration, composite-dictionary-add value
person['name'] = 'George'

#variable declaration, composite-dictionary-add value
person['eye_color'] = 'blue'

#log statement, composite-tuples-access value, 
print(fruit[2])

#conditional if
if num1 > 45:
    #log statement, 
    print("It's greater")
#conditional else
else:
    #log statement
    print("It's lower")

#condition if 
if len(string) < 5:
    #log statement
    print("It's a short word!")
#conditional else if
elif len(string) > 15:
    #log statement
    print("It's a long word!")
#conditional else
else:
    #log statement
    print("Just right!")

#for loop - start
for x in range(5):
    #for loop - stop, break, log statement
    print(x)

#for loop - start
for x in range(2,5):
    #for loop - stop, break, log statement
    print(x)

#for loop - start
for x in range(2,10,3):
    #for loop - stop, break, log statement
    print(x)

#variable declaration
x = 0
#while loop - start
while(x < 5):
    #log statement
    print(x)
    #while loop increment, stop
    x += 1

#composite - list - delete value
pizza_toppings.pop()

#composite - list - delete value
pizza_toppings.pop(1)

#log statement
print(person)

#composite - list - delete value
person.pop('eye_color')

#log statement
print(person)

#for loop - start
for topping in pizza_toppings:
    #conditional if, variable declaration
    if topping == 'Pepperoni':
        #for loop - continue
        continue
    #log statement
    print('After 1st if statement')
    #conditional if, variable declaration
    if topping == 'Olives':
        #for loop - break
        break

#function - parameter, log statement
def print_hello_ten_times():
    #for loop - start
    for num in range(10):
        #log statement
        print('Hello')

#function - argument
print_hello_ten_times()

#function - parameter
def print_hello_x_times(x):
    #for loop - start
    for num in range(x):
        #log statement
        print('Hello')

#function - argument
print_hello_x_times(4)

#function - parameter
def print_hello_x_or_ten_times(x = 10):
    #for loop - start
    for num in range(x):
        #log statement
        print('Hello')

#function - argument
print_hello_x_or_ten_times()

#function - argument
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# print(num3) 
# NameError: name <variable name> is not defined

# num3 = 72 
# variable declaration

# fruit[0] = 'cranberry' 
# TypeError: 'tuple' object does not support item assignment

# print(person['favorite_team']) 
# KeyError: 'favorite_team'

# print(pizza_toppings[7]) 
# IndexError: list index out of range

#   print(boolean)
# IndentationError: unexpected indent

# fruit.append('raspberry')
# AttributeError: 'tuple' object has no attribute 'append'

# fruit.pop(1)
#AttributeError: 'tuple' object has no attribute 'pop'