__author__ = 'talluri'

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)
        return self.balance
    def withdraw(self, amount):
        self.balance -= int(amount)
        return self.balance
    def statement(self):
        print "a/c balance is %s", self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance
    def withdraw(self, amount):
        if self.balance - int(amount) < int(self.minimum_balance):
            print "can't with draw the amount %s" % amount
        else:
            BankAccount.withdraw(self,amount)

Tarun = BankAccount()
Siddu = BankAccount()
Tarun.deposit("20")
Siddu.deposit("40")
Siddu.withdraw("10")
Tarun.withdraw("5")
Tarun.statement()
Siddu.statement()

Shanmukh = MinimumBalanceAccount("10")
Shanmukh.deposit("30")
Shanmukh.withdraw("10")
Shanmukh.withdraw("30")
Shanmukh.statement()



