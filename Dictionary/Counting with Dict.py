##Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
def Dict(string):
    count ={}
    for i in string:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    return count

string = 'abababac'
Count = Dict(string)
print(Count)
