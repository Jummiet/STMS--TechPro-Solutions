# auth.py
import sqlite3  # Import SQLite module to work with SQLite database(s)

def login(username, password):
    conn = sqlite3.connect('test_data.db')  # Connect to the SQLite database
    cur = conn.cursor()  # Create a cursor object to execute SQL commands
    cur.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))  # Query the user's role
    result = cur.fetchone()  # Fetch the first result of the query
    conn.close()  # Close the database connection
    return result[0] if result else None  # Return role if user found, otherwise None
