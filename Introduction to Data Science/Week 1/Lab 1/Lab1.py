import time
import os

def clear_console():
    """ Clears the terminal for Windows and Linux systems """
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a,b, log = False):
    """ Adds two numbers with optional logging """
    result = a+b
    if log:
        print(a, "+", b, "=", result)
    return result

def multiply(a,b, log = False):
    """ Multiplies two numbers with optional logging """
    result = a*b
    if log:
        print(a, "*", b, "=", result)
    return result

def display_menu_with_history(choice_history):
    """ Displays the menu with the history side by side """
    width = 40 
    
    lines = [
        "Welcome to Python Programming",
        "",
        "Select one of the following options:",
        "1. Add",
        "2. Multiply", 
        "3. Assign name",
        "4. Register age",
        ""
    ]
    
    # Show the last 10 choices
    history_lines = ["Choice History:", "=" * 15] + choice_history[-10:]
    
    # Print menu and history side by side
    max_lines = max(len(lines), len(history_lines))
    for i in range(max_lines):
        menu_text = lines[i] if i < len(lines) else ""
        history_text = history_lines[i] if i < len(history_lines) else ""
        print(f"{menu_text:<{width}} | {history_text}")
    return input("Enter your choice: ")

def main():
    """ Main function """
    choice_history = []
    while True:
        try:
            clear_console()
            choice = display_menu_with_history(choice_history)

            if choice == "1":
                choice_history.append("Add")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result = add(a,b, log = True)
                choice_history[-1] += f" ({a}+{b}={result})"
            elif choice == "2":
                choice_history.append("Multiply")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result = multiply(a,b, log = True)
                choice_history[-1] += f" ({a}*{b}={result})"
            elif choice == "3":
                name = input("Enter your name: ")
                choice_history.append("Name: " + name.capitalize())
            elif choice == "4":
                age = input("Enter your age: ")
                choice_history.append("Age: " + age)
            else:
                print("Invalid choice")
                continue

            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nProgram stopped")
            break

if __name__ == "__main__":
    main()
