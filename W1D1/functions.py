#What is a function? 
#set of instructions that can be called
#they make take in parameters 
#they will always return something -- even if it's None

def say_hello(times=3,name="Bob"):
    for i in range(times):
        print(f"Hello {name}")
    return "This is my return"
    

say_hello(5,"pikachu")

say_hello(10)
say_hello()

#default parameters
# must come after non-defaulted params
#named arguments
print(say_hello(name="Bob",times=5))