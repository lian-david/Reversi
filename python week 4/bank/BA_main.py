from bank_account import BankAccount
from current_account import CurrentAccount

# account1 = BankAccount(1)
# print(account1.account_num)
# account1.deposit(1000)
# #same customer id so same person has two accounts 
# account2 = BankAccount(1)
# print(account2.account_num)

# higher_acc = BankAccount.compare_accs(account1, account2)
# print(higher_acc)

# account3 = BankAccount.new_acc("bankaccount.txt")
# print(account3)

# account4 = CurrentAccount(1, 1000)
# account4.deposit(2000)
# account4.withdraw(500)
# print(account4.get_balance())
# account4.withdraw(1200)

account5 = BankAccount(10)
account5.deposit(1000)
account5.save()
account6 = BankAccount.load("account1.dat")
print(account6)

account5.withdraw(1000)