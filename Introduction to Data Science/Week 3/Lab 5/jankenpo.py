import random

def rollD3(sides):
    """ Returns a random number between 1 and sides """
    return random.randint(1, sides)

# Get user choice
print("*** Welcome to Jankenpo ***")
print("Choose a hand gesture: ")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
userChoice = input("Enter your choice: ")

# Get computer choice
computerChoice = rollD3(3)

# Determine winner
if userChoice == str(computerChoice):
    print("It's a tie!")
elif userChoice == "1" and computerChoice == 2:
    print("You lose!")
elif userChoice == "1" and computerChoice == 3:
    print("You win!")
elif userChoice == "2" and computerChoice == 1:
    print("You win!")
elif userChoice == "2" and computerChoice == 3:
    print("You lose!")
elif userChoice == "3" and computerChoice == 1:
    print("You lose!")
elif userChoice == "3" and computerChoice == 2:
    print("You win!")
else:
    print("Invalid choice")