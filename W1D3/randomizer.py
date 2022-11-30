import random
import time

groups = [
1,
2,
3,
4,
5,
6
]

input("Randomizer started. Hit enter to pull a group")
while(len(groups) > 0):
    print("Drum roll please",end="")
    for i in range(5):
        time.sleep(0.5)
        if i <= 3:
            print(". ", end="", flush=True)
        else:
            print(". \n")
    chosen = random.choice(groups)
    groups.remove(chosen)
    print("*" * 20)
    if len(groups) == 0:
        print(f"Lastly, we have {chosen}")
        print("*" * 20)
    else:
        print(f"Hey, group {chosen} you're up!  \n Remaining groups: {groups}")
        print("*" * 20)
        input("Again? \n")