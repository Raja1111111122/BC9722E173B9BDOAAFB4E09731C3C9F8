"Implement a class called BankAccount that represents a bank account. The class

should have private

attributes for account number, account holder name, and account balance. Include methods to

deposit money, withdraw money, and display the account balance. Ensure that the

account balance cannot be accessed directly from outside the class. Write a program to create an

instance of the

BankAccount class and test the deposit and withdrawal functionality."

class BankAccount:

def __init__(self, account_number, account_holder_name, initial_balance=0.0):

self account_number = account_number self._account_holder_name = account holder_name

self._account_balance initial balance

def deposit (self, amount):

if amount > 0:

self account balance += amount

#self._account_balance = self._account_balance+amount

print("Deposited (). New balance: 0.format(amount, self account balance))

else:

print("Invalid deposit amount.") def withdraw(self, amount):

if amount > 0 and amount <= self._account_balance: self._account_balance = amount

#self._account_balance= self._account_balance-amount print("Withdrew (). New balance: 0 format(amount, self._account_balance))

else:

print("Invalid withdrawal amount or insufficient balance.") def display balance(self): print("Account balance for () (Account #()): ()".format(

self._account_holder_name, self._account_number,

self account balance))

# Create an instance of the BankAccount class

account BankAccount (account_number="123456789".

account_holder_name="Hari Prabu",

initial balance 5000.0)

# Test deposit and withdrawal functionality account.display_balance()

account.deposit (500.0)

account withdraw(200.0) account withdraw(20000.0)