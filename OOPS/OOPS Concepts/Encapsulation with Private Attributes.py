class BankAccount :
    def __init__(self, account_number, balance):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self,amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance
    
    def check(self):
        return self.__balance

b = BankAccount (133907, 30000)
print(b.deposit(500))
print(b.withdraw(50))
print(b.check())
        
    
