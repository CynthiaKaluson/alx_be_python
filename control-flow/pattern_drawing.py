#!/usr/bin/env python3
"""
Drawing Patterns with Nested Loops
Uses while loops and nested for loops to draw text-based patterns
"""


def main():
    try:
        # Prompt user for pattern size
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer!")
            return

        # Draw the pattern using nested loops
        row = 0
        while row < size:
            # Use for loop to print asterisks in each row
            for col in range(size):
                print("*", end="")
            print()  # Move to next line after each row
            row += 1

    except ValueError:
        print("Please enter a valid positive integer!")


if __name__ == "__main__":
    main()