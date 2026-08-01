class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_ano(self):
        return self.__account_number
    def set_ano(self, new):
        self.__account_number = new
        

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new):
        if new <0:
            print("Cannot be negative")
        else:
            self.__balance = new
        

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

a =SavingsAccount(10763, 30000, 12)
print(a.get_ano(), a.get_balance(), a.interest_rate)
a.set_ano(2836)
a.set_balance(5000)
print(a.get_ano(), a.get_balance(), a.interest_rate)
