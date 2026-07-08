def func(file_path):
    with open ( file_path,'r') as file:
       count = file.readlines()
       l_c = len(count)
       w_c = sum(len(word.split()) for word in count)
       c_c = sum(len(word) for word in count)
    return l_c,w_c,c_c

file_path = 'sample.txt'
result = func(file_path)
print(result)
    
