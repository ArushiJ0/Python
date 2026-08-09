def singleton(cls):
    instance = {}

    def get_instance(*args , **kwargs):

        if cls not in  instance:
            instance[cls] = cls(*args, **kwargs)
            return instance[cls]
    return get_instance
        

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Database created")


db1= DatabaseConnection()

db2= DatabaseConnection()

print(db1 is db2)


        
