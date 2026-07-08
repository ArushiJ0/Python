##Write a function that splits a large file named `large.txt` into smaller files of 100 lines each.

def splitting_large(file_name, lines):
    with open(file_name , 'r') as main:
        content = main.readlines()
        for i in range(0,len(content), lines):
            with open(f'{file_name} {i//lines+1}.txt','w' ) as file:
                file.writelines( content [i: i+lines])

splitting_large('sample_300_lines.txt',100)
            
