import math

# Advanced Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate the square root of a negative number."
    return math.sqrt(x)

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation (x^y)")
    print("6. Modulus (x % y)")
    print("7. Square Root")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {exponentiate(num1, num2)}")
            elif choice == '6':
                print(f"The result is: {modulus(num1, num2)}")

        elif choice == '7':
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            print(f"The result is: {square_root(num)}")

        else:
            print("Invalid choice! Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the Advanced Calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()