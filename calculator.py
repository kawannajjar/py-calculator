"""
This file contains the main functions for the calculator.
Available functions:
- Add
- Subtract
- Multiply
- Divide
"""


def add(a, b):
    """
    This function adds two numbers.
    :param a: First number
    :param b: Second number
    :return: Sum of the two numbers
    """
    return a + b


def subtract(a, b):
    """
    This function subtracts the second number from the first number.
    :param a: First number
    :param b: Second number
    :return: Difference of the two numbers
    """
    return a - b


def multiply(a, b):
    """
    This function multiplies two numbers.
    :param a: First number
    :param b: Second number
    :return: Product of the two numbers
    """
    return a * b


def divide(a, b):
    """
    This function divides the first number by the second number.
    :param a: First number
    :param b: Second number
    :return: Quotient of the division
    :raises ZeroDivisionError: If the second number is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed!")
    return a / b