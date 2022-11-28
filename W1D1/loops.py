#Loops

#For loops

# for ____ in ____:

#first blank is our iterative variable -- will be different for collections
 # we will name this

#second blank is the collection we are iterating over


#range is a function that returns a sequence of numbers
# range(start,stop,step)
# start -- the number we will begin at INCLUSIVE (optional, default to 0)
# stop -- the number we will stop at EXCLUSIVE (required)
# step -- increment value --- can be negative or positive

# for number in range(100,10,-20):
#     print(number)

#iterating over a list

our_list = ['gyrados','vulpix','ninetails','pikachu','sharpedo']
our_string = "pokemon"
# for one_pokemon in our_list:
    # one_pokemon = "Gengar"
#     print(one_pokemon)
# print(our_list)

for i in range(len(our_list)):
    print(our_list[i])
    our_list[i] = "ditto"
print(our_list)

# for char in our_string:
#     print(char)

#iterating over a dict

cat1 = {
    'name': 'Cinnamon',
    'age':2,
    'color': 'orange'
}
cat2 = {
    'name': 'Meow',
    'age':2,
    'color': 'black'
}

for key in cat1:
    print(f"{key} --- {cat1[key]}")

for val in cat1.values():
    print(val)

for key,val in cat1.items():
    print(key, val)

cat_list = [cat1,cat2]

for one_cat in cat_list:
    for key in one_cat:
        print(f"{key} - {one_cat[key]}")

print(cat_list[1]['name'])
#while
"""
while condition:
    logic that works towards invalidating the condition

"""
x = 5
while x > 0:
    print("hello")
    x -= 1
