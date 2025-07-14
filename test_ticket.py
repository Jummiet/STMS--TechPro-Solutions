# test_ticket.py
import unittest
import sqlite3
from ticket import TicketSystem

class TestTicketSystem(unittest.TestCase):

    def setUp(self):
        self.username = "customer1"
        self.role = "Customer"
        self.ts = TicketSystem(self.username, self.role)

    def test_create_ticket(self):
        desc = "Test issue from unittest"
        self.ts.cur.execute("INSERT INTO tickets (customer_username, description, status, history) VALUES (?, ?, 'Open', ?)", (self.username, desc, 'Created'))
        self.ts.conn.commit()
        self.ts.cur.execute("SELECT * FROM tickets WHERE customer_username=? AND description=?", (self.username, desc))
        result = self.ts.cur.fetchone()
        self.assertIsNotNone(result)

    def test_update_ticket_description(self):
        # Insert a sample ticket first
        self.ts.cur.execute("INSERT INTO tickets (customer_username, description, status, history) VALUES (?, ?, 'Open', ?)", (self.username, 'Old Desc', 'Created'))
        self.ts.conn.commit()
        tid = self.ts.cur.lastrowid
        # Now update it
        new_desc = "Updated by test"
        self.ts.cur.execute("UPDATE tickets SET description=? WHERE ticket_id=?", (new_desc, tid))
        self.ts.conn.commit()
        self.ts.cur.execute("SELECT description FROM tickets WHERE ticket_id=?", (tid,))
        updated_desc = self.ts.cur.fetchone()[0]
        self.assertEqual(updated_desc, new_desc)

    def tearDown(self):
        self.ts.conn.close()

if __name__ == '__main__':
    unittest.main()
