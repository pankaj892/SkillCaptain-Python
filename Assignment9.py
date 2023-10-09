'''Python program that performs certain operations on a given dictionary.'''

# Create a dictionary
dict1 = {'a': 100, 'b': 200, 'c': 300}


# Add key/value pairs in dictionary
dict1['e'] = 500
print(dict1)

#Remove a key-value pair from a dictionary
del dict1['a']
print(dict1)

#Update a value of a key in a dictionary
dict1['b'] = 400
print(dict1)

#Check if a given key already exists in a dictionary
if 'b' in dict1:
    print("Key b is present and value is: ", dict1['b'])
else:
    print("Key b is not present")

#Print all the keys in a dictionary
print(dict1.keys())