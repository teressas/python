from typing import TypeAlias
# characters
# - halfings
# - dwarves
# - humans

# Action
# - info
# - attack
# - defense
# - increase health

class Character:
    def __init__(self, name, health, attack_strength, defense_strength):
        self.name = name
        self.health = health
        self.attack_strength = attack_strength
        self.defense_strength = defense_strength
    
    def info(self):
        print(f"""{f' {self.name.upper()} ':*^80}""")
        print(f"health: {self.health}")
        print(f"attack_strength: {self.attack_strength}")
        print(f"defense_strength: {self.defense_strength}")
        return self

    def attack(self, attackee:object):
        print(f"{self.name} is attacking {attackee.name}")

class Halfling(Character):
    def __init__(self, name, health=100, attack_strength=25, defense_strength=30):
        super().__init__(name, health, attack_strength, defense_strength)

class Dwarf(Character):
    def __init__(self, name, health=120, attack_strength=75, defense_strength=25):
        super().__init__(name, health, attack_strength, defense_strength)

class Human(Character):
    def __init__(self, name, health=100, attack_strength=50, defense_strength=50):
        super().__init__(name, health, attack_strength, defense_strength)

bob = Character('bob')
bob.info()

frodo = Halfling('frodo')
frodo.info()

aragorn  = Human('aragorn')
aragorn.info()

aragorn.attack()