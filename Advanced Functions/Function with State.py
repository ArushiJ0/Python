def count(call={'count':0}):
    call['count']+=1
    return call['count']
print(count())
print(count())
print(count())
