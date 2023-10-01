age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
if age >= 18 and age < 66:
    print("You are an adult")
if age >= 66:
    print("You are a senior citizen")
else:
    print("Error: Age cannot be negative")        