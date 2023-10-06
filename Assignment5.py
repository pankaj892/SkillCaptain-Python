#Program using a while loop to print all the numbers from 1 to 10

number = 1
while number <= 10:
    print(number)
    number = number + 1
print("Finished")
print('-----------------------------')

#Program using a for loop to iterate through a list of names and print them all
names = ["Google","Microsoft","Facebook","Apple","IBM","Oracle","Amazon"]
for name in names:
    print(f'Welcome to {name}!')
