import datetime
import unittest
from unittest.mock import Mock

class Bank():

    currentAccountNumber = 0
    
    def __init__(self):
        self.bankAccounts = []

    def addAccount(self):
        x = BankAccount(self.getNextAccountNumber())
        self.bankAccounts.append(x)

    def removeAccount(self, accountNumber):
        for x in self.bankAccounts:
            if x.getAccountNumber()==accountNumber:
                self.bankAccounts.remove(x)

    def getNextAccountNumber(self):
        self.currentAccountNumber += 1
        return self.currentAccountNumber

    def isValidAccountNumber(self, accountNum):
        for i in self.bankAccounts:
            if i.getAccountNumber() == accountNum:
                return True
        return False

    def getAccount(self, accountNum):
        if self.isValidAccountNumber(accountNum)==True:
            for i in self.bankAccounts:
                if i.getAccountNumber() == accountNum:
                    return i
        else:
            raise Exception("No Account Found")
        

    def printAccounts(self):
        for i in self.bankAccounts:
            print("Account number:",i.getAccountNumber(), "Balance:",i.getBalance())

    

class BankAccount():
    
    def __init__(self, number):
        self.accountNumber = number
        self.balance = 0
        self.transactions = []
        
        
    def getAccountNumber(self):
        return self.accountNumber
    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            x = Transaction('deposit', amount, datetime.date.today())
            
        else:
            print("Amount must be greater than 0")
            x = Transaction('failed - amount less than 0', amount, datetime.date.today())
        self.transactions.append(x)
        

    def withdraw(self, amount):
        if amount > 0 and self.balance-amount >= 0:
            self.balance -= amount
            x = Transaction('withdrawal', amount, datetime.date.today())
            
        elif amount > 0 and self.balance - amount < 0:
            print("You don't have enough money available")
            x = Transaction('failed - not enough money', amount, datetime.date.today())
            
        else:
            print("The amount must be greater than 0")
            x = Transaction('failed - amount less than 0', amount, datetime.date.today())
        self.transactions.append(x)


    def getBalance(self):
        return self.balance
    

    def printTransactions(self):
        print("Transactions for account #",self.accountNumber)
        for x in self.transactions:
            print(x)
        print()


class Transaction():

    def __init__(self, transactionType, amount, date):
        self.transactionType = transactionType
        self.amount = amount
        self.date = date

    def __repr__(self):
        text = ''
        if self.transactionType == 'withdrawal':
            text = 'withdrew'
        else:
            text = self.transactionType

        s = text + " $"
        s += str(self.amount) + " on "
        s += str(self.date)
        return s



# bank = Bank()
# bank.addAccount()
# bank.addAccount()

# print(bank.bankAccounts[0].getAccountNumber())
# print(bank.getAccount(1))
# print(bank.getAccount(1))
# print(bank.isValidAccountNumber(5))
# b = bank.getAccount(5)
# print(b)
# b.deposit(10)
# bank.bankAccounts[0].deposit(10)
# bank.bankAccounts[0].getBalance()

# print(bank.bankAccounts)

# bank.printAccounts()


# b.deposit(10)
# b.deposit(20)
# b.deposit(-10)
# b.withdraw(10)
# b.withdraw(-2)
# print(b.printTransactions())


# print('Next account number:',bank.getNextAccountNumber())
# print('All bank accounts:', bank.bankAccounts)
# bank.printAccounts()
                
        
