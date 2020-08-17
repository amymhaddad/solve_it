"""
Create a Loan class. Each time someone creates a new Loan, it's
    for a certain amount of money.  That money is taken from the
    bank's available assets.

    l1 = Loan(500)
    l2 = Loan(200)
    l3 = Loan(700)  # raises an exception -- ValueError to indicate no money
    l1.repay(500)
    l3 = Loan(700)  # now it'll work, because the bank has sufficient funds
"""


class Loan(object):
    bank_assets = 1000

    def __init__(self, amount):

        if Loan.bank_assets >= amount:

            self.amount_owed = amount

            Loan.bank_assets -= amount
        else:
            raise ValueError("Not enough money")

    def repay(self, repay_amount):
        self.amount_owed -= repay_amount
        Loan.bank_assets += repay_amount


l1 = Loan(500)
l2 = Loan(200)
l1.repay(500)
print(Loan.bank_assets)
