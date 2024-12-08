"""
This file runs the calculator through the command line interface.
The user can choose which mathematical operation to perform.
"""

from calculator import add, subtract, multiply, divide


def main():
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Please enter your choice (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print(f"Result of addition: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result of subtraction: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result of multiplication: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"Result of division: {divide(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()