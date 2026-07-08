##Write a function that reads the contents of a file named `sample.txt` and prints each line.

def read(file_path):
    with open(file_path , 'r') as file:
        for lines in file:
            print(lines.strip())

read('sample.txt')
