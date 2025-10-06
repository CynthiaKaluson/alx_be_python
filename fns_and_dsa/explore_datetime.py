#!/usr/bin/env python3
"""
Explore datetime Module
Demonstrates working with dates and times in Python
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(days):
    """
    Calculate future date by adding days to current date

    Args:
        days (int): Number of days to add

    Returns:
        datetime: Future date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date


def main():
    """Main function to run the datetime exploration"""
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(days)

    except ValueError:
        print("Please enter a valid number of days!")


if __name__ == "__main__":
    main()