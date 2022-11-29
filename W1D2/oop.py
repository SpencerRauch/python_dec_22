#OOP Objects and Classes!

#object? an instance of a class that comes with the attributes (describing values) and methods (things an object can do)
#that are described in the class

#Class? template / blue print for our instances / objects -- custom data type

dog_1 = {
    'name': 'Mochi',
    'age': 3,
    'breed': "malti poo"
}

dog_2 = {
    'name': "Paloma",
    'age': 2,
    'breed': 'jack russel'
}
#attributes are describing factors of an object
#methods being what objects can do
class Dog:
    all_dogs = []
    # def __init__(self,name_param,age,breed):
    #     self.name = name_param
    #     self.age = age
    #     self.breed = breed
    def __init__(self,dict, roommate=None):
        self.name = dict['name']
        self.age = dict['age']
        self.breed = dict['breed']
        self.roommate = roommate

        Dog.all_dogs.append(self)

    def bark(self):
        print(f"{self.name} makes a loud bork!")
        return self

    def birthday(self):
        self.age = self.age +1
        #self.age += 1
        print(f"{self.name} gets a year older! They are now {self.age} year(s) old {Dog.convert_years_to_dog_years(self.age)} in dog years")

    def __repr__(self):
        return f"{self.name} is a dog object {self.breed}"

    def greet_roommate(self):
        if self.roommate == None:
            print("The dog looks around, doesn't see anyone, they're doing great on their own though")
        else:
            print(f"{self.name} approaches {self.roommate.name}")
            self.roommate.say_hello()

    @classmethod
    def bark_party(cls):
        for one_dog in cls.all_dogs:
            one_dog.bark()

    @staticmethod
    def convert_years_to_dog_years(years):
        return years * 7

    @staticmethod
    def is_valid(dictionary):
        is_valid = True
        if dictionary['name'] == "":
            is_valid = False
        return is_valid

class Human:
    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")
    

me = Human("Spencer")

# dog_3 = Dog("Mochi",3,"malti poo")
# dog_4 = Dog("Paloma", 2, "jack russel")
dog_3 = Dog(dog_1, me)
independent_dog = Dog(dog_1)
# dog_4 = Dog(dog_2)
# print(dog_3.name)
# print(dog_4.name)
# print(dog_3)

# None.bark()
dog_3.birthday()
# dog_3.name = "blue"


#Class methods
"""
do not have access to instance attributes
can access class attributes
no reference to self
call it from the class itself
"""

#Static methods 
"""
stationary / non-changing
no access to anything! 
validations / utility
"""

Dog.bark_party()

# if Dog.is_valid(dog_1):
#     dog5 = Dog(dog_1)

# dog_3.roommate = me

print(dog_3.roommate.name)
dog_3.greet_roommate()
independent_dog.greet_roommate()

