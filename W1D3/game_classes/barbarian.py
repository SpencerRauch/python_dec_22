from game_classes.human import Human

class Barbarian(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength += 5
        self.health += 20
        self.defense -= 4

    def berserker_rage(self,target):
        target.defend(self.strength*2)
        self.defend(self.strength)
        print(f"{self.name} swings wildly, harming everyone")
        print(f"{target.name} now has {target.health}")
        print(f"{self.name} now has {self.health}")