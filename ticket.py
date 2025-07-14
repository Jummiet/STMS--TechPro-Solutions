# ticket.py
import sqlite3  # Import SQLite module

class TicketSystem:
    def __init__(self, username, role):
        self.username = username  # Store the current user's username
        self.role = role  # Store the current user's role
        self.conn = sqlite3.connect('test_data.db')  # Connect to the database
        self.cur = self.conn.cursor()  # Create a cursor for executing SQL commands

    def customer_menu(self):
        while True:
            print("\n1. Create Ticket\n2. View My Tickets\n3. Update My Ticket\n4. Exit")  # Display options
            choice = input("Choose an option: ")  # Prompt user for choice
            if choice == '1':
                desc = input("Describe your issue: ")  # Get ticket description from user
                self.cur.execute("INSERT INTO tickets (customer_username, description, status, history) VALUES (?, ?, 'Open', ?)", (self.username, desc, 'Created'))  # Insert new ticket
                self.conn.commit()  # Save changes
                print("Ticket submitted successfully.")  # Acknowledge submission
            elif choice == '2':
                self.cur.execute("SELECT * FROM tickets WHERE customer_username=?", (self.username,))  # Fetch user's tickets
                for t in self.cur.fetchall():
                    print(t)  # Display each ticket
            elif choice == '3':
                tid = input("Enter the Ticket ID you want to update: ")  # Ask for ticket ID
                self.cur.execute("SELECT * FROM tickets WHERE ticket_id=? AND customer_username=?", (tid, self.username))  # Fetch specific ticket
                ticket = self.cur.fetchone()  # Get ticket data
                if ticket:
                    print("Current Description:", ticket[2])  # Show current description
                    print("1. Update Description\n2. Mark as Resolved\n3. Cancel")  # Update options
                    action = input("Choose an action: ")  # Get action from user
                    if action == '1':
                        new_desc = input("Enter new description: ")  # Get new description
                        self.cur.execute("UPDATE tickets SET description=?, history=history || ';Description updated' WHERE ticket_id=?", (new_desc, tid))  # Update description
                        self.conn.commit()  # Save changes
                        print("Description updated.")  # Confirm update
                    elif action == '2':
                        self.cur.execute("UPDATE tickets SET status='Resolved', history=history || ';Resolved by customer' WHERE ticket_id=?", (tid,))  # Mark ticket as resolved
                        self.conn.commit()  # Save changes
                        print("Ticket marked as resolved.")  # Confirm resolution
                    else:
                        print("Update cancelled.")  # Cancel update
                else:
                    print("Ticket not found or you are not authorized to update it.")  # Error message
            else:
                break  # Exit loop

    def engineer_menu(self):
        while True:
            print("\n1. View Assigned Tickets\n2. Update Ticket Status\n3. Exit")  # Display menu options
            choice = input("Choose an option: ")  # Get user choice
            if choice == '1':
                self.cur.execute("SELECT * FROM tickets WHERE assigned_to=?", (self.username,))  # Get assigned tickets
                for t in self.cur.fetchall():
                    print(t)  # Display tickets
            elif choice == '2':
                tid = input("Enter Ticket ID to update: ")  # Prompt for ticket ID
                new_status = input("New Status: ")  # Prompt for new status
                self.cur.execute("UPDATE tickets SET status=?, history=history || ';Status changed to ' || ? WHERE ticket_id=?", (new_status, new_status, tid))  # Update ticket
                self.conn.commit()  # Save changes
                print("Ticket updated.")  # Confirm update
            else:
                break  # Exit menu

    def admin_menu(self):
        while True:
            print("\n1. View All Tickets\n2. Assign Ticket\n3. Exit")  # Display admin options
            choice = input("Choose an option: ")  # Prompt admin for choice
            if choice == '1':
                self.cur.execute("SELECT * FROM tickets")  # Get all tickets
                for t in self.cur.fetchall():
                    print(t)  # Display tickets
            elif choice == '2':
                tid = input("Enter Ticket ID: ")  # Prompt for ticket ID
                engineer = input("Assign to Engineer Username: ")  # Prompt for engineer username
                self.cur.execute("UPDATE tickets SET assigned_to=?, history=history || ';Assigned to ' || ? WHERE ticket_id=?", (engineer, engineer, tid))  # Assign ticket
                self.conn.commit()  # Save changes
                print("Ticket assigned.")  # Confirm assignment
            else:
                break  # Exit menu

    def __del__(self):
        self.conn.close()  # Ensure the database connection is closed when object is deleted