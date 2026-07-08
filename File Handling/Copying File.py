##Write a function that copies the contents of a file named `source.txt` to a new file named `destination.txt`.

def copying(file_name, copy_name):
    with open(file_name , 'r') as file:
        content = file.read()

    with open(copy_name , 'w') as file:
        file.write(content)

copying('sample.txt','destination.txt')
