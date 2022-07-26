from bank_account import BankAccount

class CurrentAccount(BankAccount):
    """The current account
    """
    def __init__(self, customer_id, transaction_limit):
        super().__init__(customer_id)
        self.transaction_limit = transaction_limit

    def __str__(self):
        return super().__str__() + f', Transaction limit: {self.transaction_limit}'

    def withdraw(self, funds):
        if funds > self.transaction_limit:
            raise ValueError("Amount exceeds the allowed withdrawal limit.")
        super().withdraw(funds)