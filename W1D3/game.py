from game_classes.barbarian import Barbarian
from game_classes.cleric import Cleric
import random


barb = Barbarian("Conan")
cler = Cleric("Bob")


print("You are the barbarian, you approach a cleric")
while barb.health > 0 and cler.health > 0:
    response = ""
    while not response == "1" and not response == "2":
        response = input("What do? 1)attack 2)REALLY ATTACK \n>>>")
        if response == "1":
            barb.attack(cler)
        elif response == "2":
            barb.berserker_rage(cler)
        else:
            print("Please choose a valid option")
    dice_roll = random.randint(1,2)
    if dice_roll == 1:
        cler.attack(barb)
    else:
        cler.heal()

if barb.health > 0:
    print("Congrats, you won!")
elif cler.health <=0:
    print("Draw")
else:
    print("The cleric has defeated you")
