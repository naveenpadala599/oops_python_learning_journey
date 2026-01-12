class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self._balance=balance
    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
    def withdraw(self, amount):
        if amount<=self._balance:
            self._balance-=amount
        else:
            print("Insufficient funds.")
    def display(self):
        print("Available funds:",self._balance)
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        self._balance+=self._balance*self.interest_rate
acc=SavingsAccount("Naveen", 1000, 0.05) 
acc.deposit(2000)
acc.add_interest()
acc.withdraw(3000)
acc.display()
            
            
    
