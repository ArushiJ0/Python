##Write a function that merges the contents of multiple files into a single file named `merged.txt`.

def merging (files , merged_file):
    with open(merged_file, 'w') as mfile:
        for i in files:
            with open(i ,'r') as file:
                mfile.write(file.read()+ '\n')
                

merging(['destination.txt','output.txt'],'merged.txt') 
