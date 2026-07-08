##Write a function that appends a given string to the end of a file named `log.txt`.

def appending(file_name, text):
    with open (file_name , 'a') as file:
        file.write(text + '\n')


appending('sample.txt','\n new line appended')
