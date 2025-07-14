## Overview
The TechPro Service Ticket Management System is a command-line Python application designed for a fictional tech support company, TechPro Solutions. It simulates a real-world ticketing workflow, supporting three roles:
- Admin – full access to all tickets and assignments
- Support Engineer – access to and management of assigned tickets
- Customer – can create, view, and update their tickets

It uses object-oriented design, SQLite for data storage, and features a modular, maintainable structure.


## System Requirements
1. Python 3.7+
2. SQLite (included with Python)
3. VS Code (recommended with SQLite extension)

## Setup Instructions
1. Clone or extract the project folder
2. Make sure all files (main.py, auth.py, ticket.py, setup_db.py, etc.) are in the same directory.
3. Install SQLite Viewer Extension (optional but helpful)
4. In VS Code, search for “SQLite” by alexcvzz or “SQLite Viewer” in Extensions.
5. Initialize the database
  
    bash
    python setup_db.py
   
7. This creates test_data.db with:
- User accounts (Admin, Engineer, Customers)
- Sample service tickets


## Running the application

  bash
  python main.py


## Sample Login Credentials

Role	              Username
Admin	              admin
Support Engineer	  engineer1
Customer	          customer1	
Customer	          customer2


## Functional Features
# Login & Role-Based Access
- Authenticates user credentials via auth.py
- Returns appropriate menu for the user’s role

# Ticket System Features (ticket.py)
For Customers:
- Create new service tickets
- View existing tickets
- Update ticket descriptions or mark as resolved

For Support Engineers:
- View tickets assigned to them
- Update ticket statuses (e.g., “In Progress”, “Resolved”)

For Admins:
- View all tickets
- Assign tickets to support engineers
  

## Testing
Run test scripts using:
    bash
    python test_auth.py
    python test_ticket.py

Or all at once:
    bash
    python -m unittest discover


# Test coverage includes:
- Valid/invalid logins
- Ticket creation
- Ticket updates

## Database Schema
# users Table
Column	      Type	     Description
id	          INTEGER	   Auto-increment primary key
username	    TEXT	     Unique login ID
password	    TEXT	     Login password
role	        TEXT	     Role: Admin, Support Engineer, Customer

# tickets Table
Column	              Type	       Description
ticket_id	            INTEGER	     Auto-increment primary key
customer_username	    TEXT	       User who created the ticket
description	          TEXT	       Issue description
status	              TEXT	       Ticket status (Open, In Progress, etc.)
assigned_to	          TEXT	       Username of assigned engineer (if any)
history	              TEXT	       Semicolon-separated update history



## Reflection & Learning Outcomes
This project demonstrates:
- Use of object-oriented programming in real-world modeling
- Importance of modularity and code reuse
- Basic SQLite database management
- Principles of role-based access control
- Value of structured testing in software development

## File Structure
- main.py          # Entry point and CLI interface
- auth.py          # Handles login and authentication
- ticket.py        # Contains the TicketSystem class for all roles
- setup_db.py      # Sets up SQLite DB with sample data
- test_data.db     # Database file (created after setup)
- test_auth.py     # Unit tests for login
- test_ticket.py   # Unit tests for ticket operations
- README.md        # This document
- user_manual.txt  # Role-specific usage instructions
- reflection.txt   # Developer insights and project summary
