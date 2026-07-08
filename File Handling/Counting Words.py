##Write a function that reads the contents of a file named `document.txt` and returns the number of words in the file.

def counting(file_name):
    with open(file_name,'r') as file:
        line = file.read()
        word = line.split()
        
    return len(word)

print(counting('sample.txt'))
        
            
        
