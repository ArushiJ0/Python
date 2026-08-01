class Product:
    def __init__(self , product_id , name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_pid(self):
        return self.__product_id
    def set_pid(self, new):
        self.__product_id = new
        

    def get_name(self):
        return self.__name
    def set_name(self, new):
        self.__name = new
        

    def get_price(self):
        return self.__price
    def set_price(self, new):
        if new<0:
            print("Can;t be negative")
        else:
            self.__price = new
       

p = Product(2076, 'Butter' , 80)
print(p.get_pid(), p.get_name(), p.get_price())
p.set_pid(8726), p.set_name('Cookie'), p.set_price(70)
print(p.get_pid(), p.get_name(), p.get_price())
    
    
