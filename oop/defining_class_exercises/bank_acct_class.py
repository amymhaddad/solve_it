"""
Create a BankAccount class. It'll have a single
attribute (per instance), transactions -- a list of floats

Every time you deposit, append a positive float
Every time you withdraw, append a negative float

(a) create two different accounts
(b) add a number of transactions +/- to each account
(c) show, for each account, the number of transactions
and the average amount per transaction, as well as
the current balance.  (assume it starts at 0)
"""
import math


class BankAccount:
    def __init__(self):
        self.transactions = [0]


deposits = BankAccount()
withdraws = BankAccount()

deposits.transactions.append(88.88)
deposits.transactions.append(79.88)
withdraws.transactions.append(-45.34)


def total_deposits(deposits):
    return sum(1 for deposit in deposits.transactions if deposit > 0)


def total_withdraws(withdraws):
    return sum(1 for withdraws in withdraws.transactions if withdraws < 0)


def withdraws_details(total_withdraws, withdraws, deposits):
    average_withdraw_amount = sum(withdraws.transactions) // 2
    current_balance = sum(withdraws.transactions + deposits.transactions)
    return {
        "total_withdraws": total_withdraws(withdraws),
        "average_transaction_amount": average_withdraw_amount,
        "current_balance": f"{current_balance:.2f}",
    }


def deposit_details(total_deposits, withdraws, deposits):
    average_deposit_amount = sum(deposits.transactions) // 2
    current_balance = sum(withdraws.transactions + deposits.transactions)
    return {
        "total_deposits": total_deposits(deposits),
        "average_transaction_amount": average_deposit_amount,
        "current_balance": f"{current_balance:.2f}",
    }
