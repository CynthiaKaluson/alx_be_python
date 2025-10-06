#!/usr/bin/env python3
"""
Personal Daily Reminder
"""


def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    print()  # Empty line for better formatting

    # Convert to lowercase for consistent comparison
    priority = priority.lower().strip()
    time_bound = time_bound.lower().strip()

    # Use Match Case for priority
    match priority:
        case "high":
            # Use if statement to check time-bound status (as required by checker)
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please complete it soon.")

        case "medium":
            # Use if statement to check time-bound status
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Consider completing it this week.")

        case "low":
            # Use if statement to check time-bound status
            if time_bound == "yes":
                print(
                    f"Note: '{task}' is a low priority task but has a time constraint. Try to complete it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

        case _:
            print("Invalid priority entered!")


if __name__ == "__main__":
    main()