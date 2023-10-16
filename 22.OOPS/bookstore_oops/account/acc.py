class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!!")
        else:
            self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account): #base class passed as argument this is inheritance
    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)
    
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("account//balance.txt", 10)
checking.deposit(100)
print(checking.balance)
checking.transfer(100)
checking.commit()
print(checking.balance)

# harsh_account = Account("account//balance.txt")
# print(harsh_account.balance)
# harsh_account.withdraw(90)
# print(harsh_account.balance)
# harsh_account.deposit(100)
# print(harsh_account.balance)
# harsh_account.commit()