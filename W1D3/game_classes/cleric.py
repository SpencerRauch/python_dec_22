# from game_classes import human
from game_classes.human import Human

class Cleric(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength -= 2
        self.mana = 14
        self.defense = 4

    def attack(self, target):
        # super().attack(target)
        print(f"{self.name} pray for {target.name} to be injured")
        target.defend(self.mana)
    
    def heal(self):
        print(f"{self.name} heals self for {self.mana/2}")
        self.health += self.mana/2
        print(f"{self.name} now has {self.health}")
        


