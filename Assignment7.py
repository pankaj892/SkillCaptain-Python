""" Function that takes an integer as input and returns True if the number is even, and False otherwise."""

def is_even(number):
    '''Function to check if a number is even or odd'''
    return bool(number % 2 == 0 is True)   # if the remainder of the number divided by 2 is 0, then the number is even else it will be odd 

number = int(input("Enter a number: ")) # asks the user to enter a number
print(is_even(number)) # prints the result of the function
print('Done')
print('------------------')