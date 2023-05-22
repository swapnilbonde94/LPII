# Define an empty dictionary to store the information
information = {}

# Function to add information
def add_information(key, value):
    information[key] = value
    print("Information added successfully.")

# Function to delete information
def delete_information(key):
    if key in information:
        del information[key]
        print("Information deleted successfully.")
    else:
        print("Information not found.")

# Function to display all information
def display_information():
    if information:
        print("Information:")
        for key in information:
            print(f"{key}: {information[key]}")
    else:
        print("No information available.")

# Function to search for information
def search_information(key):
    if key in information:
        print(f"{key}: {information[key]}")
    else:
        print("Information not found.")

# Main program loop
while True:
    print("\n--- Information Management Expert System ---")
    print("1. Add information")
    print("2. Delete information")
    print("3. Display information")
    print("4. Search information")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        add_information(key, value)
    elif choice == "2":
        key = input("Enter key to delete: ")
        delete_information(key)
    elif choice == "3":
        display_information()
    elif choice == "4":
        key = input("Enter key to search: ")
        search_information(key)
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")