# LIST - Literally Indexed, Single Things (Stores one item at an index)
# DICT - Don't Index, Coupled Things (Stores key value pairs) "Curlies hold the keys"

# Definition:

list = ['red','blue','green'] # indices 0, 1, 2

dict = {
    'color1': 'red',
    'color2': 'blue',
    'color3': 'green'
}

#Access:
#notice both use brackets but dict uses keys, list uses indices
list[2] #green
dict['color3'] #green

#Assignment

list[2] = 'pink' #updates third index to 'pink'
dict['color3'] = 'pink' #updates value stored paired with key 'color3' to 'pink'

#Adding to list/dict
list.append("orange")
dict['color4'] = 'orange'

#Removing from list/dict
list.pop(2) #pop an index
del list[2] #removes index 2 without returning it

color2 = dict.pop('color2') #pop a KVP by key and return it

del dict['color4'] #deletes on KVP without returning it
dict.clear() #clears whole dict
