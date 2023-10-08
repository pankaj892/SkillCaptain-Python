""" Function that takes an integer as input and returns True if the number is even, and False otherwise."""

def is_even(number):
    if number % 2 == 0:   # if the remainder of the number divided by 2 is 0, then it is even
        return True
    return False      # if the remainder of the number divided by 2 is not 0, then it is odd

number = int(input("Enter a number: ")) # asks the user to enter a number
print(is_even(number)) # prints the result of the function
print('Done')
print('------------------')