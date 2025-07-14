# main.py
from auth import login  # Import the login function from auth module
from ticket import TicketSystem  # Import the TicketSystem class from ticket module

def main():
    print("Welcome to TechPro Solutions Service Ticket Management System")  # Welcome message
    username = input("Username: ")  # Prompt user to enter username
    password = input("Password: ")  # Prompt user to enter password
    role = login(username, password)  # Call login function to validate credentials and get user role

    if not role:
        print("Login failed. Please check your credentials.")  # Inform user of failed login
        return  # Exit the function

    print(f"\nWelcome {username}! Role: {role}\n")  # Display welcome message with role
    ts = TicketSystem(username, role)  # Create an instance of TicketSystem with current user info

    if role == 'Customer':
        ts.customer_menu()  # Show customer menu
    elif role == 'Support Engineer':
        ts.engineer_menu()  # Show support engineer menu
    elif role == 'Admin':
        ts.admin_menu()  # Show admin menu

if __name__ == '__main__':
    main()  # Run the main function if this script is executed directly
