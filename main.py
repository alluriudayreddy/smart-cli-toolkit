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


def Unit_converter():
    print("\nWelcome to the Unit Converteer!")
    print("1.kilometers to miles")
    print("2. miles to kilometers")
    print("3. Celsius to Farenheit")
    print("4. farenheit to Celsius")
    print("5. millimeters to inches")
    print("6. inches to millimeters")
    print("7. Kilograms to Grams")
    print("8. Grams to Kilograms")
    print("9. Kilograms to Pounds")
    print("10. Pounds to Kilograms")
    print("11. Celsius to Fahrenheit")
    print("12. Fahrenheit to Celsius")

    choice = int(input("Select a conversion type: "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        result = value * 0.621371
        print(f"{value} kilometers is equal to {result} miles.")
    elif choice == 2:
        result = value / 0.621371
        print(f"{value} miles is equal to {result} kilometers.")
    elif choice == 3:
        result = (value * 9/5) + 32
        print(f"{value} Celsius is equal to {result} Farenheit.")
    elif choice == 4:
        result = (value - 32) * 5/9
        print(f"{value} Farenheit is equal to {result} Celsius.")
    elif choice == 5:
        result = value * 0.0393701
        print(f"{value} millimeters is equal to {result} inches.")
    elif choice == 6:
        result = value / 0.0393701
        print(f"{value} inches is equal to {result} millimeters.")
    elif choice == 7:
        result = value * 1000
        print(f"{value} Kilograms is equal to {result} Grams.")
    elif choice == 8:
        result = value / 1000
        print(f"{value} Grams is equal to {result} Kilograms.")
    elif choice == 9:
        result = value * 2.20462
        print(f"{value} Kilograms is equal to {result} Pounds.")
    elif choice == 10:
        result = value / 2.20462
        print(f"{value} Pounds is equal to {result} Kilograms.")
    elif choice == 11:
        result = (value * 9/5) + 32
        print(f"{value} Celsius is equal to {result} Fahrenheit.")
    elif choice == 12:
        result = (value - 32) * 5/9
        print(f"{value} Fahrenheit is equal to {result} Celsius.")
    else:
        print("Invalid conversion type!")


def Random_Number_Generator():
    print("\nWelcome to the Random Number Generator!")
    start = int(input("Enter the start of the rnage: "))
    end =  int(input("Enter the end of the range: "))

    random_number = random.randint(start, end)
    print(f"Generated random number between {start} and {end} is: {random_number}")


def notes_tool():
    print("\nNOTES TOOL")
    note = input("Write your note here: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully.")


menu_bar()
user_choice = int(input("Select a number to run the tool: "))
while user_choice != 0:
    
    if user_choice == 1:
        Calculator()
    elif user_choice == 2:
        Password_generator()
    elif user_choice == 3:
        Unit_converter()
    elif user_choice == 4:
        Random_Number_Generator()
    elif user_choice == 5:
        notes_tool()
    else:
        print("Invalid option. Please try again.")
    
    menu_bar()
    user_choice = int(input("Select a number to run the tool: "))

print("\nExiting SMART CLI TOOLKIT.")
print("Thank you for using. Goodbye!")
