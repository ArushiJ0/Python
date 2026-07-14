##Create a class named `BankAccount` with private attributes `account_number` and `balance`. Add methods to deposit and withdraw money, and to check the balance. Create an object of the class and perform some operations.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
           self.__balance +=  amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient")
        else:
           self.__balance -=  amount

    def check_balance(self):
        return self.__balance
    
acc = BankAccount( 1875439, 5000)
acc.deposit(500)
acc.withdraw(300)
print(acc.check_balance())

        
        
        
