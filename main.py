import random
import string

def menu_bar():
    print("\nSMART CLI TOOLKIT")
    print("1. Calculator")
    print("2. Password Generator")
    print("3. Unit Converter")
    print("4. Random Number Generator")
    print("5. Notes Tool")
    print("0. Exit")


def Calculator():
    print("\nWelcome to the Calculator!")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operator == "+":
        print("Result: ", num1 + num2)
    elif operator == "-":
        print("Result: ", num1 - num2)
    elif operator == "*":
        print("Result: ", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result: ", num1 / num2)
        else:
            print("Can't divide by zero!")
    else:
        print("Invalid operator!")


def Password_generator():
    print("\nWelcome to the Password Generator!")
    length = int(input("Enter the required length of the password: "))
    characters =  string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    print("Generated password:", password)
menu_bar()
user_choice = int(input("Select a number to run the tool: "))
while user_choice != 0:
    
    if user_choice == 1:
        Calculator()
    elif user_choice == 2:
        Password_generator()
    elif user_choice == 3:
        pass #call unit converter function here
    elif user_choice == 4:
        pass # call random number generator fucntion here
    elif user_choice == 5:
        pass # calll notes tool function here
    else:
        print("Invalid option. Please try again.")
    
    menu_bar()
    user_choice = int(input("Select a number to run the tool: "))

print("\nExiting SMART CLI TOOLKIT.")
print("Thank you for using. Goodbye!")
