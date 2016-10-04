#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Account:
    pass

def deposit(acct, amount):
    if amount <= 0:
        raise ValueError('must be positive')
    acct.balance += amount
       
def withdraw(acct, amount):
    if amount <= acct.balance:
        acct.balance -= amount
    else:
        raise RuntimeError('balance not enough')

acct = Account()
acct.number = '123-456-789'
acct.name = 'Justin'
acct.balance = 0

print(acct.number)    # 123-456-789
print(acct.name)      # Justin

deposit(acct, 100)
print(acct.balance)   # 100
withdraw(acct, 50)
print(acct.balance)   # 50
