#!/usr/bin/env python3
"""
Personal Daily Reminder
Uses conditional statements, Match Case, and loops for task reminders
"""


def main():
    # Prompt for a single task
    task = input("Enter your task: ").strip()

    # Get priority with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").lower().strip()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter 'high', 'medium', or 'low'")

    # Get time-bound status with validation loop
    while True:
        time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()
        if time_bound_input in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'")

    # Convert time-bound input to boolean
    time_bound = time_bound_input == 'yes'

    # Process the task based on priority and time sensitivity
    print()  # Empty line for better formatting

    # Use Match Case for priority handling
    match priority:
        case "high":
            if time_bound:
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please complete it soon.")

        case "medium":
            if time_bound:
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Consider completing it this week.")

        case "low":
            if time_bound:
                print(
                    f"Note: '{task}' is a low priority task but has a time constraint. Try to complete it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")


if __name__ == "__main__":
    main()