##Write a function that attempts to write a list of strings to a file. Use try, except, and finally blocks to handle IOError and ensure the file is properly closed.

def file_writing(file_name , text):
    try:
        file = open(file_name , 'w')
        file.writelines(text)
    except IOError as e:
        print(e)
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
            print("File Closed")

file_writing('new.txt', ['HI', 'I', 'am','XYZ'])
        
