"""
Models for Account Service
"""

class Account:
    """Account class"""

    accounts = {}
    counter = 1

    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email

    def create(self):
        """Creates an Account"""
        self.id = Account.counter
        Account.counter += 1
        Account.accounts[self.id] = self
        return self

    def update(self):
        """Updates an Account"""
        if self.id is None:
            raise ValueError("Account ID is not set")

        self.__class__.accounts[self.id] = self

    def delete(self):
        """Deletes an Account"""
        if self.id in self.__class__.accounts:
            del self.__class__.accounts[self.id]

    @classmethod
    def find(cls, account_id):
        """Finds an Account by its ID"""
        return cls.accounts.get(account_id)

    @classmethod
    def list_all(cls):
        """Lists all Accounts"""
        return list(cls.accounts.values())