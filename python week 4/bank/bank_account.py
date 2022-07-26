from with_exception import InvalidWithdrawal
import pickle

class BankAccount:
    """This class represents a Bank Account, where the user can deposit and
        withdraw funds. 
    """
    last_account_num = 0        #stores the last allocated account number, this is class attribute 

    def __init__(self, customer_id):
        """Initializes the customer id, account number, and balance 
            of the bank account

        Args:
            custumer_id(int): the customer id
            account_number(int): the account number associated with the customer
            balance(int): the balance of the account
        """
        self.customer_id = customer_id
        BankAccount.last_account_num += 1
        self.account_num = BankAccount.last_account_num
        self.balance = 0

    def deposit(self, amt_money):
        self.balance += amt_money

    def withdraw(self, funds):
        if self.balance > funds:
            self.balance -= funds
        else:
            raise InvalidWithdrawal(funds)

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f'The custumer id is {self.customer_id}, with account number {self.account_num}, and a balance of {self.balance}'

    @staticmethod
    def compare_accs(acc1, acc2):
        if acc1.balance > acc2.balance:
            return acc1
        else:
            return acc2
    
    @classmethod
    def new_acc(cls, source_file):
        with open(source_file) as f:
            customer_id = int(f.readline())
            account_num = int(f.readline())
        
        account = cls(customer_id)
        account.account_num = account_num
        return account

    def save(self):
        #save the account to a file named account[num].dat
        file_path = f'account{self.account_num}.dat'
        with open(file_path, "wb") as f:
            pickle.dump(self, f)
    
    @classmethod        #can also be static method
    def load(cls, file_path):
        with open(file_path, "rb") as f:
            account = pickle.load(f)
            return account


    
