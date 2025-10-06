#!/usr/bin/env python3
"""
Multiplication Table Generator
Uses a for loop to generate and print multiplication table
"""


def main():
    try:
        # Prompt user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print multiplication table using for loop
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")

    except ValueError:
        print("Please enter a valid number!")


if __name__ == "__main__":
    main()