num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

addition = num1 + num2
print(f"Addition: {addition}")

subtraction = num2 - num1
print(f"Subtraction: {subtraction}")

multiplication = num1 * num2
print(f"Multiplication: {multiplication}")

try:
    if num2 == 0:
        print("Error: Cannot divide by zero")
except:
    division = num1 / num2
    print(f"Division: {division}")

