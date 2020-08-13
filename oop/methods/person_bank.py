""""
Use our existing Person and BankAccount classes.  Make it possible
for a person to have one or more bank accounts.  So we can say:

p1.add_account(ba1)
p1.add_account(ba2)

p1.all_balances()           # returns a list of floats representing balances
p1.current_total_balance()  # gives the total balance across all accounts

p1.average_transaction_amount()  # returns the average amount of transactions across all accounts


"""


class Person(object):
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.bank_accounts = []

    def add_account(self, account):
        self.bank_accounts.append(account)

    def all_balances(self):
        return [sum(account.transactions) for account in self.bank_accounts]

    def current_total_balance(self):
        return sum(self.all_balances())

    def average_transaction_amount(self):
        all_transactions = sum(
            [
                one_transaction
                for one_account in self.bank_accounts
                for one_transaction in one_account.transactions
            ]
        )
        return all_transactions // 2


class BankAccount(object):
    def __init__(self):
        self.transactions = []


p1 = Person("bob", "bob@example.com", "123-45-6789")
checking = BankAccount()
checking.transactions.append(20)
checking.transactions.append(200)
checking.transactions.append(-100)


savings = BankAccount()
savings.transactions.append(200)
checking.transactions.append(2000)
checking.transactions.append(-1000)

p1.add_account(checking)
p1.add_account(savings)

print(p1.all_balances())
print(p1.current_total_balance())
print(p1.average_transaction_amount())
