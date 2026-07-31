class BankAccount:
    def __init__(self, account_number , balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance (self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount<0:
            print("Cannot be negative")
        else:
            self.__balance = amount

b = BankAccount (1938, 3000)
print(b.balance)
b.balance = -990
