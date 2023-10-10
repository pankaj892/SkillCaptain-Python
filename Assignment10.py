'''Python program to perform conversions between a list and a set'''

# Create a list
my_list = [1, 2, 3, 4, 5]

def list_to_set(list):
    '''Function to convert a list to a set'''
    return set(list)

def set_to_list(set):
    '''Function to convert a set to a list'''
    return list(set)

print(list_to_set(my_list))
print(set_to_list(list_to_set(my_list)))