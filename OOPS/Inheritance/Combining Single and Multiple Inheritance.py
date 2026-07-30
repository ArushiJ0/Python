class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self,brand, model):
        super().__init__(brand)
        self.model = model

class Camera:
    def __init__(self, resolution):
        self.resolution =  resolution

class Smartphone(Phone , Camera):
    def __init__( self,brand,model,resolution):
        Phone.__init__(self,brand ,model)
        Camera.__init__(self,resolution)

s = Smartphone('Samsung',17471, '44x')
print(s.brand, s.model,s.resolution)
