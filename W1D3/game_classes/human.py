class Human:
    def __init__(self):
        self.name = "Generic Human"
        self.health = 100
        self.strength = 10
        self.mana = 10
        self.defense = 5

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}")
        target.defend(self.strength)

    def defend(self, damage):
        damage -= self.defense
        self.health -= damage
        print(f"{self.name} takes {damage} and now has {self.health}")