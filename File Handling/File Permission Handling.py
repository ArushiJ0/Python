##Write a function that attempts to read a file named `protected.txt` and handles any permission errors gracefully by printing an error message.
def protected_file(file_name):
    try:
        with open(file_name,'r')as file:
            file.read()
    except PermissionError as e:
        print(f'The file is protected {e}')

protected_file('sample.txt')
