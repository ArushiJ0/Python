##Write a function that finds and replaces all occurrences of a given word in a file named `data.txt` with another word.

def find_replace(file_name, old , new):
    with open(file_name, 'r') as file:
        content = file.read()
        new_text = content.replace(old, new)

    with open(file_name ,'w') as file:
        file.write(new_text)

find_replace('sample.txt', 'line', 'word')
