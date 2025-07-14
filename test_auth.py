# test_auth.py
import unittest
from auth import login

class TestAuth(unittest.TestCase):

    def test_valid_login_admin(self):
        self.assertEqual(login("admin", "admin123"), "Admin")

    def test_valid_login_engineer(self):
        self.assertEqual(login("engineer1", "eng123"), "Support Engineer")

    def test_invalid_password(self):
        self.assertIsNone(login("admin", "wrongpass"))

    def test_nonexistent_user(self):
        self.assertIsNone(login("ghostuser", "somepass"))

if __name__ == '__main__':
    unittest.main()
