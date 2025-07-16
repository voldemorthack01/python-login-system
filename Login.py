import getpass  # Used to hide password input when typing

# File where account data will be stored
ACCOUNTS_FILE = "accounts.txt"

# Reads account data from the file and returns a dictionary {username: password}
def update_data():
    try:
        # Read lines from the file, ignoring blank lines
        with open(ACCOUNTS_FILE, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
        data = {}
        for line in lines:
            if ',' in line:
                # Split each line into username and password using comma
                username, password = line.split(",", 1)
                data[username] = password
        return data
    except FileNotFoundError:
        # If file doesn't exist, return empty dictionary
        print("File not found. Starting with empty data.")
        return {}

# Saves the account data dictionary to the file in comma separated format
def save_data(data):
    with open(ACCOUNTS_FILE, "w") as file:
        for user, pwd in data.items():
            file.write(f"{user},{pwd}\n")

# Handles account creation, validating input and saving the new user
def create_account(data):
    while True:
        username = input("Enter the new username: ").strip() # "Strip" cleans the whitespace from username
        if username == "": # Check if username is empty
            print("Username cannot be empty.")
        elif "," in username: # Check if username contains a comma since it would break the CSV format (CSV = Comma Separated Values)
            print("Username cannot contain commas.")
        elif username in data: # Check if username already exists
            print("Username already exists. Please choose a different one.")
        else:
            break

    while True:
        password = getpass.getpass("Enter the new password: ") # Use getpass to hide password input
        if len(password) < 10: # Password must be at least 10 characters long
            print("Password must be at least 10 characters long.")
        else:
            break

    # Add new user to the data dictionary and save to file
    data[username] = password
    save_data(data)
    print("New account created successfully.")

# Logs in a user by checking credentials
def login(data):
    while True:
        username = input("Enter your username: ").strip() # "Strip" cleans the whitespace from username
        if username not in data: # Check if username exists in the data
            print("Username not found.")
        else:
            password = getpass.getpass("Enter your password: ") # Use getpass to hide password input
            if password == data[username]:  # Check if password matches
                print("Login successful!")
                return username
            else:
                print("Incorrect password. Please try again.")

# Allows a logged-in user to change their password
def change_password(data, user):
    old_password = getpass.getpass(f"Enter your old password for user ({user}): ")  # Use getpass to hide old password input
    if old_password != data[user]:  # Check if old password matches
        print("Incorrect old password.")
        return

    while True:
        new_password = getpass.getpass("Enter your new password: ") # Use getpass to hide new password input
        if len(new_password) < 10:  # Check if new password is at least 10 characters long
            print("Password must be at least 10 characters long.")
            continue
        confirm_password = getpass.getpass("Re-enter your new password: ")  # Use getpass to hide confirmation password input
        if new_password != confirm_password:    # Check if new password matches confirmation
            print("Passwords do not match. Try again.")
        else:
            break

    # Update password and save
    data[user] = new_password
    save_data(data)
    print("Password updated successfully.")

# Allows a logged-in user to change their username
def change_username(data, old_user):
    while True:
        new_username = input("Enter your new username: ").strip()   # "Strip" cleans the whitespace from username
        if new_username == "":  # Check if new username is empty
            print("Username cannot be empty.")
        elif "," in new_username:   # Check if new username contains a comma
            print("Username cannot contain commas.")
        elif new_username in data:  # Check if new username already exists
            print("Username already exists. Please choose a different one.")
        else:
            break

    # Change username by transferring password and removing old user
    data[new_username] = data.pop(old_user)
    save_data(data)
    print(f"Username changed from {old_user} to {new_username}")
    return new_username

# Allows a logged-in user to delete their account after confirmation
def delete_account(data, user):
    confirm = input(f"Are you sure you want to delete your account '{user}'? (yes/no): ").lower()   # Ask for confirmation
    if confirm == "yes":  # Check if user confirmed deletion
        del data[user]  # Remove user from data
        save_data(data) # Save updated data to file
        print("Account deleted successfully.")
        return True
    else:
        print("Account deletion cancelled.")
        return False

# Displays menu options for a logged-in user
def user_menu(data, user):
    while True:
        print(f"\nWelcome, {user}!")    
        print("1. Change Password")
        print("2. Change Username")
        print("3. Delete Account")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":   # Change password
            change_password(data, user)
        elif choice == "2": # Change username
            user = change_username(data, user)  # Username might change, so update variable
        elif choice == "3": # Delete account
            if delete_account(data, user):  # If account is deleted, exit loop
                break
        elif choice == "4": # Logout
            print("Logged out.")
            break
        else:   # Invalid choice
            print("Invalid choice.")

# Main menu for users who are not logged in
def main_menu():
    data = update_data()  # Load current account data
    while True:
        print("\nWelcome to the Account Manager!")
        print("1. Create a new account")
        print("2. Login to an existing account")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":   # Create a new account
            create_account(data)
            data = update_data()  # Refresh data after account creation
        elif choice == "2": # Login to an existing account
            user = login(data)
            user_menu(data, user)
            data = update_data()  # Refresh data in case anything changed in user menu
        elif choice == "3": # Exit the program
            print("Exiting the program.")
            break
        else:   # Invalid choice
            print("Invalid choice. Please try again.")

# Run the program
main_menu()