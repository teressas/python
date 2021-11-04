class Pet:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks #can expand this a make a list or object and make it interface
        self.health = 100
        self.energy = 100
        self.noise = noise

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)

class dog(Pet):
    def __init__(self, name, type, tricks, power):
        super().__init__(self, name, type, tricks)
        self.power = power
        

