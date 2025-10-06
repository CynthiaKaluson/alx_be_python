#!/usr/bin/env python3
"""
Shopping List Manager
Uses Python lists to manage a shopping list
"""


def display_menu():
    """Display the main menu options"""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """Main function to run the shopping list manager"""
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add item to the list
            item = input("Enter the item to add: ").strip()
            if item:  # Check if item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty. Please try again.")

        elif choice == '2':
            # Remove item from the list
            if not shopping_list:  # Check if list is empty
                print("The shopping list is empty. Nothing to remove.")
            else:
                print("Current shopping list:", shopping_list)
                # Case-insensitive removal
                item_to_remove = input("Enter the item to remove: ").strip().lower()
                found = False
                for item in shopping_list:
                    if item.lower() == item_to_remove:
                        shopping_list.remove(item)
                        print(f"'{item}' has been removed from the shopping list.")
                        found = True
                        break
                if not found:
                    print(f"'{item_to_remove}' was not found in the shopping list.")

        elif choice == '3':
            # View the current list
            if not shopping_list:  # Check if list is empty
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()