import unittest
from service.models import Account


class TestAccountModel(unittest.TestCase):

    def setUp(self):
        Account._accounts = []
        Account._counter = 0

    def test_create_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        result = account.create()

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, "Abhi")

    def test_update_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        account.name = "Updated Abhi"
        account.update()

        updated = Account.find(account.id)

        self.assertEqual(updated.name, "Updated Abhi")

    def test_delete_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        account.delete()

        found = Account.find(account.id)

        self.assertIsNone(found)

    def test_find_an_account(self):
        account = Account("Abhi", "abhi@gmail.com")
        account.create()

        found = Account.find(account.id)

        self.assertIsNotNone(found)
        self.assertEqual(found.email, "abhi@gmail.com")

    def test_list_all_accounts(self):
        account1 = Account("Abhi", "abhi@gmail.com")
        account2 = Account("Ram", "ram@gmail.com")

        account1.create()
        account2.create()

        accounts = Account.list_all()

        self.assertEqual(len(accounts), 2)


if __name__ == "__main__":
    unittest.main()