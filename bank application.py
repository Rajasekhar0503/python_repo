import sys
class customer:
    'customer class with bank operations.....'
    bankname='unionbank'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance+= amt
    def withdraw(self,amt):
        if amt>self.balance:
            print('isufficent funds....cannot perform this operation')
            sys.exit()
        self.balance-= amt
        print('balance after withdraw:',self.balance)
print('welcome to',customer.bankname)
name=input('enter your name:')
c=customer(name)
while True:
    print('d=deposit\nw=withdraw\ne=exit')
    option=input('enter your option:')
    if option=='d':
        amt=float(input('enter amount:'))
        c.deposit(amt)
    elif option=='w':
        amt=float(input('enter amount:'))
        c.withdraw(amt)
    elif option=='e':
        print('thanks for banking')
        sys.exit()
    else:
        print('invalid option....pls choose valid option')

    