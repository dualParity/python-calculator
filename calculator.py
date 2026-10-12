#!/usr/bin/env python3
"""
Simple Python Calculator
A basic calculator that supports addition, subtraction, multiplication, and division.
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    return a ** b


def square_root(a):
    """Calculate square root"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return a ** 0.5


def calculator():
    """Interactive calculator function"""
    print("=" * 50)
    print("Welcome to Python Calculator")
    print("=" * 50)
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square Root")
    print("7. Exit")
    print("\n" + "=" * 50)

    while True:
        try:
            choice = input("\nSelect operation (1/2/3/4/5/6/7): ").strip()

            if choice == '7':
                print("\nThank you for using the calculator. Goodbye!")
                break

            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"\n{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"\n{num1} ** {num2} = {power(num1, num2)}")

            elif choice == '6':
                num = float(input("Enter number: "))
                print(f"\n√{num} = {square_root(num)}")

            else:
                print("Invalid choice. Please select 1-7.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    calculator()
