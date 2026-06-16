def return_type(List):
    INT = list(filter(lambda x:isinstance(x,int),List))
    STR = list(filter(lambda x:isinstance(x,str),List))
    FL =list(filter(lambda x:isinstance(x,float),List))
    return INT , STR,FL
List=[1,2,3,'a','b',76.98,90.8,'string' , 8, 97.6]
print(return_type(List))
