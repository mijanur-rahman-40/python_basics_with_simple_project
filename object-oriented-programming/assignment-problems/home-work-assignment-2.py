class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print('Deposit Accepted')

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)
print(acct1.balance)
