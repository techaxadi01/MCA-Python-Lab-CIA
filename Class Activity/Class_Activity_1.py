class Account:
    account_no = 100001

    def __init__(self, name, balance):
        self.name = name
        self.acc_no = Account.account_no
        self.balance = balance
        Account.account_no += 1

    def display(self):
        print()
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)
        print()

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)


class SavingsAccount(Account):
    def interest(self):
        interest = self.balance * 5 / 100
        self.balance = self.balance + interest
        print("Interest Recived:", interest)


class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("ERROR : Insufficient Balance")


# Creating objects
John = SavingsAccount("John", 5000)
Marina = CurrentAccount("Marina", 10000)

print()

# Savings Account
print("Savings Account")
John.display()
John.deposit(1000)
John.interest()
John.display()

print()

# Current Account
print("Current Account")
Marina.display()
Marina.deposit(2000)
Marina.withdraw(3000)
Marina.display()

print()