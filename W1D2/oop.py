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
    # def __init__(self,name_param,age,breed):
    #     self.name = name_param
    #     self.age = age
    #     self.breed = breed
    def __init__(self,dict):
        self.name = dict['name']
        self.age = dict['age']
        self.breed = dict['breed']

    def bark(self):
        print(f"{self.name} makes a loud bork!")
        return self

    def birthday(self):
        self.age = self.age +1
        #self.age += 1
        print(f"{self.name} gets a year older! They are now {self.age} year(s) old")

    def __repr__(self):
        return f"{self.name} is a dog object {self.breed}"

        
# dog_3 = Dog("Mochi",3,"malti poo")
# dog_4 = Dog("Paloma", 2, "jack russel")
dog_3 = Dog(dog_1)
dog_4 = Dog(dog_2)
# print(dog_3.name)
# print(dog_4.name)
print(dog_3)

# None.bark()
dog_3.birthday()
dog_3.color = "blue"



