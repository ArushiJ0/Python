def temp(T,unit):
    if unit == 'C':
       return (T*(9/5)) + 32
    else:
        return(T -32) *(5/9)
       

print(temp(978,'F'))
        
