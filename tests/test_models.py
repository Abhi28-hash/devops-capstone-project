import unittest
from service.models import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        Account.data = {}
        Account.ids = iter(range(1000))

    def test_create_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        self.assertIsNone(account.id)

        account.create()

        self.assertIsNotNone(account.id)
        self.assertEqual(account.id, 0)

    def test_read_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        found = Account.find(account.id)

        self.assertEqual(found.id, account.id)
        self.assertEqual(found.name, account.name)
        self.assertEqual(found.email, account.email)

    def test_update_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        account.name = "Abhi Updated"
        account.update()

        updated = Account.find(account.id)

        self.assertEqual(updated.name, "Abhi Updated")

    def test_delete_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        account.delete()

        found = Account.find(account.id)

        self.assertIsNone(found)

    def test_list_all_accounts(self):
        account1 = Account("Abhi", "abhi@gmail.com")
        account1.create()

        account2 = Account("John", "john@gmail.com")
        account2.create()

        accounts = Account.list_all()

        self.assertEqual(len(accounts), 2)

if __name__ == "__main__":
    unittest.main()