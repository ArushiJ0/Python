##Write a function that writes a list of strings to a file named `output.txt`, with each string on a new line.

def write(file_name, text):
    with open(file_name ,'w') as file:
        for line in text:
            file.write(line + '\n ')

text = ['HI','How are you ?']
write('output.txt', text)
        
