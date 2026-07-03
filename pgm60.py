class BankAccount:
    def __init__(self):
        
        self.__balance = 12000
        
    def deposit(self, amount):
        
        self.__balance = self.__balance + amount
        print("Amount Deposited")
        
    def withdraw(self, amount):
        
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")
    def display(self):
       print("Current Balance:", self.__balance)
acc = BankAccount()
acc.deposit(2000)  
acc.withdraw(3000)  
acc.display()  