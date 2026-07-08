##Write a function that reads a binary file named `image.bin` and writes its contents to another binary file named `copy_image.bin`.

def bin_file(file_name , copy_name):
    with open(file_name ,'rb') as file:
        content = file.read()
    with open(copy_name ,'wb') as cfile:
        cfile.write(content)

bin_file('b_file.bin' , 'copy_b_file.bin')
