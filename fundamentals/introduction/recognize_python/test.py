name = 12
print("My name is", name)

name = "Zen"
print("My name is " + name)

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

x = "hello hello"
print(x.title())
# output:
"Hello World"

print(x.count(x))

dog = ("Canis Familiaris", "dog", "carnivore", 12)

dog = dog[:3] + ("man's best friend",) + dog[4:]
print(dog)
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

