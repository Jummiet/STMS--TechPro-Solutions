import sqlite3
import os

# Check if DB already exists
db_path = "test_data.db"
if os.path.exists(db_path):
    print("Database already exists at:", db_path)
else:
    print("Creating new database:", db_path)

# Connect to the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Create users table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Admin', 'Support Engineer', 'Customer'))
)
''')

# Create tickets table
cur.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_username TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    assigned_to TEXT,
    history TEXT
)
''')

# Inserts sample users
cur.executemany('''
INSERT OR IGNORE INTO users (username, password, role)
VALUES (?, ?, ?)
''', [
    ("admin", "admin123", "Admin"),
    ("engineer1", "eng123", "Support Engineer"),
    ("engineer2", "eng456", "Support Engineer"),
    ("engineer3", "eng789", "Support Engineer"),
    ("engineer4", "eng321", "Support Engineer"),
    ("engineer5", "eng654", "Support Engineer"),
    ("customer1", "cust123", "Customer"),
    ("customer2", "cust456", "Customer"),
    ("customer3", "cust789", "Customer"),
    ("customer4", "cust321", "Customer"),
    ("customer5", "cust654", "Customer")
])

# Insert sample tickets
cur.executemany('''
INSERT INTO tickets (customer_username, description, status, assigned_to, history)
VALUES (?, ?, ?, ?, ?)
''', [
    ("customer1", "Internet not working", "Open", None, "Created"),
    ("customer2", "Computer won’t start", "In Progress", "engineer1", "Assigned to engineer1;Status changed to In Progress"),
    ("customer3", "Unable to connect to company VPN", "Open", None, "Created"),
    ("customer4", "Email client crashes on startup", "Open", None, "Created"),
    ("customer5", "Printer not responding after Windows update", "In Progress", "engineer1", "Assigned to engineer1;Status changed to In Progress"),
    ("customer1", "Slow system performance with new antivirus", "Open", None, "Created"),
    ("customer2", "Forgotten login credentials for internal portal", "Resolved", "engineer1", "Assigned to engineer1;Resolved credentials issue"),
    ("customer3", "Software installation issue", "Resolved", "engineer1", "Assigned to engineer1;Resolved issue")
])

conn.commit()
conn.close()

print("Database setup complete and saved as 'test_data.db'")
