def add(a, b):
    """ Adds two numbers """
    return a + b
def subtract(a, b):
    """ Subtracts two numbers """
    return a - b
def multiply(a, b):
    """ Multiplies two numbers """
    return a * b
def divide(a, b):
    """ Divides two numbers """
    return a / b
def exponentiate(a, b):
    """ Raises a number to the power of another number """
    return a ** b

print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")

userChoice = input("(1) Add two numbers\n (2) Subtract two numbers\n (3) Multiply two numbers\n (4) Divide two numbers\n (5) Exponentiate two numbers\n")
firstNumber = int(input("Type the first number:"))
secondNumber = int(input("Type the second number:"))

match userChoice:
    case "1":
        result = add(firstNumber, secondNumber)
        print(f"The addition of {firstNumber} and {secondNumber} is {result}")
    case "2":
        result = subtract(firstNumber, secondNumber)
        print(f"The subtraction of {firstNumber} and {secondNumber} is {result}")
    case "3":
        result = multiply(firstNumber, secondNumber)
        print(f"The multiplication of {firstNumber} and {secondNumber} is {result}")
    case "4":
        result = divide(firstNumber, secondNumber)
        print(f"The division of {firstNumber} and {secondNumber} is {result}")
    case "5":
        result = exponentiate(firstNumber, secondNumber)
        print(f"The exponentiation of {firstNumber} and {secondNumber} is {result}")
    case _:
        print("Invalid menu choice.")
