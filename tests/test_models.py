"""
Test cases for Account Model
"""

import unittest
from service.models import Account


class TestAccount(unittest.TestCase):
    """Test Cases for Account"""

    def setUp(self):
        Account.accounts = {}
        Account.counter = 1

    def test_create_an_account(self):
        """It should Create an Account"""

        account = Account("Abhi", "abhi@gmail.com")
        self.assertIsNone(account.id)

        account.create()

        self.assertIsNotNone(account.id)
        self.assertEqual(account.id, 1)

    def test_find_account(self):
        """It should Find an Account by ID"""

        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        found = Account.find(account.id)

        self.assertEqual(found, account)

    def test_update_an_account(self):
        """It should update an Account"""

        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        account.name = "Abhishek"
        account.email = "abhishek@gmail.com"
        account.update()

        updated = Account.find(account.id)

        self.assertEqual(updated.name, "Abhishek")
        self.assertEqual(updated.email, "abhishek@gmail.com")

    def test_delete_an_account(self):
        """It should Delete an Account"""

        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        account.delete()

        found = Account.find(account.id)

        self.assertIsNone(found)

    def test_list_all_accounts(self):
        """It should List all Accounts"""

        account1 = Account("Abhi", "abhi@gmail.com")
        account1.create()

        account2 = Account("John", "john@gmail.com")
        account2.create()

        accounts = Account.list_all()

        self.assertEqual(len(accounts), 2)


if __name__ == "__main__":
    unittest.main()