print("Hello December Cohort!")

x = 5
if x > 50:
    pass

# This is a comment

"""
This is a comment
that can be on multiple lines
"""

#Variables ?

snake_case = "All lower case, separated by underscore"
GLOBAL_VAR = "All caps"
#class names will be pascal case ie HumanClass

#Datatypes 

#Primitive
#number

integer = 8
float_num = 8.6

#string ' '  " "

string = "A collection of characters!"
format_string = f"We can inject variables {integer} "
concat_str = "Can we do this " + str(integer)
# print(concat_str)
# print(format_string)

#boolean

bool = True
bool2 = False


#Composite

#lists - what we call arrays in js, zero indexed
num_list = [1,2,3,4,5,6,7,8]
      # 0 1 2 3 4 5 6 7
val = num_list[7]
num_list[7] = 100
print(num_list)
#Literally Indexed Single Thing
#num_list functions
len(num_list) #returns the length
min(num_list)
max(num_list)

#num_list methods
num_list.append(1337)
print(num_list)
num_list.pop(2) #pop will remove by index
print(num_list)
num_list.remove(100) #remove will remove by value
num_list.sort(reverse=True)
print(num_list)


#dictionaries
#Don't Index, Coupled Things
#Key Value Pairs
dog_dict = {
    'name': 'Mochi',
    'age': 3,
    'breed': "Pitbull"
}
print(dog_dict)
# name = dog_dict['size']
name = dog_dict['name']
print(name)
#if *key* in *dictionary*:
if "name" in dog_dict:
    print(f"The dogs name is {dog_dict['name']}")
if "size" in dog_dict:
    print(f"The dogs size is {dog_dict['size']}")
else: 
    print("Size not found")

dog_dict['size'] = "big boi"

#removing from a dict
del dog_dict['age']
breed = dog_dict.pop('breed')
dog_dict.clear()


#tuples
#immutable list ? Cannot be changed
tup = (1,2,3,5)
tup[3] = 163546 #cannot do this causes an error


#if
#else
#elif

x = 8

if x == 5:
    print("x is 5")
elif x > 5:
    print("x is big")
else:
    print("x is small")

"""
Py        Js
==        ===
None      Null
not       !
or        ||
and       &&
is <-- is is used to check if both operands are the same object

"""
