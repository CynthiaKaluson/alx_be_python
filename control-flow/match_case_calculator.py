#!/usr/bin/env python3
"""
Simple Calculator with Match Case
Uses Match Case statements for handling multiple operations
"""


def main():
    # Prompt for user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Perform calculation using Match Case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation! Please choose from +, -, *, /")


if __name__ == "__main__":
    main()