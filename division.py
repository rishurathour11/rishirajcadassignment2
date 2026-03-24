# Division Program

# taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# checking division by zero
if num2 == 0:
    print("Division by zero is not allowed")
else:
    result = num1 / num2
    print("The result is:", result)
