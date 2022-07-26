from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_id, interest_rate=0.01):
        super().__init__(customer_id)
        self.interest_rate = interest_rate

    def add_interest_rate(self):
        self.balance *= (1 + self.interest_rate)