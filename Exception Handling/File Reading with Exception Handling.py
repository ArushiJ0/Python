##Write a function that reads the contents of a file named `data.txt`. Use try, except, and finally blocks to handle file not found errors and ensure the file is properly closed.

def file_ex(file_name):
    try:
        file = open(file_name ,'r')
        print(file.read())
    except FileNotFoundError as e:
        print(e)
    finally:
        if 'file' in locals () and not file.closed:
            file.close()
            print('File is closed')
file_ex('data.txt')
