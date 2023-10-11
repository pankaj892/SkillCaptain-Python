""" Python program that concatenates two lists into a single list."""

list1 = [1,2,3,5] # asks the user to enter a number
list2 = [1.7,5,1,80,9] # asks the user to enter a number

def concat_lists(list1, list2):
    '''Function to concatenate two lists'''
    return list1 + list2

print(concat_lists(list1, list2)) # prints the result of the function