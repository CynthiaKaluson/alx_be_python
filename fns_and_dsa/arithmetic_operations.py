#!/usr/bin/env python3
"""
Arithmetic Operations Function
Defines perform_operation function for basic arithmetic
"""


def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations

    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation type - 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: Result of operation or error message for division by zero
    """
    operation = operation.lower().strip()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."