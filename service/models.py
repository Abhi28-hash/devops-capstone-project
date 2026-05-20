class Account:

    _accounts = []
    _counter = 0

    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email

    def create(self):
        Account._counter += 1
        self.id = Account._counter
        Account._accounts.append(self)
        return self

    def update(self):
        for idx, account in enumerate(Account._accounts):
            if account.id == self.id:
                Account._accounts[idx] = self
                return self

    def delete(self):
        Account._accounts = [
            account for account in Account._accounts
            if account.id != self.id
        ]

    @classmethod
    def find(cls, account_id):
        for account in cls._accounts:
            if account.id == account_id:
                return account
        return None

    @classmethod
    def list_all(cls):
        return cls._accounts