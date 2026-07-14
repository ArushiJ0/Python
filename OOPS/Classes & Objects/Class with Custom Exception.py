##Create a custom exception named `InsufficientBalanceError`. In the `BankAccount` class, raise this exception when a withdrawal amount is greater than the balance. Handle the exception and print an appropriate message.


class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceError ("Withdrawl cannot happen")
        else:
            self.balance -= amount

acc = BankAccount(3000)
try:
    acc.withdraw(500)
    
except InsufficientBalanceError  as e:
    print(e)
    

