from itertools import count

class Account:

    ids = count(0)
    data = {}

    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email

    def create(self):
        self.id = next(Account.ids)
        Account.data[self.id] = self
        return self

    def update(self):
        Account.data[self.id] = self

    def delete(self):
        del Account.data[self.id]

    @classmethod
    def find(cls, account_id):
        return cls.data.get(account_id)

    @classmethod
    def list_all(cls):
        return list(cls.data.values())