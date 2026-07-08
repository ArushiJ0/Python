##Write a function that reads the contents of a file named `reverse.txt` and prints each line in reverse order.

def reverse(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
        for line in reversed(content):
            print (line.strip())

reverse('sample.txt')

