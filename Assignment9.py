'''Python program that performs certain operations on a given dictionary.'''

# Create a dictionary
my_dict = {'a': 100, 'b': 200, 'c': 300}


# Add key/value pairs in dictionary
my_dict['e'] = 500
print(my_dict)

#Remove a key-value pair from a dictionary
del my_dict['a']
print(my_dict)

#Update a value of a key in a dictionary
my_dict['b'] = 400
print(my_dict)

#Check if a given key already exists in a dictionary
if 'b' in my_dict:
    print("Key b is present and value is: ", my_dict['b'])
else:
    print("Key b is not present")

#Print all the keys in a dictionary
print(my_dict.keys())