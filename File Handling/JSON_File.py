##Write a function that reads a JSON file named `data.json` and prints its contents as a Python dictionary.

import json

def json_file(file_name):
    with open(file_name , 'r') as file:
        content = json.load(file)
        return(content)


print(json_file('json_file.json'))
