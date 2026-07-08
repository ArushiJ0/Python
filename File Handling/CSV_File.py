##Write a function that reads a CSV file named `data.csv` and prints its contents as a list of dictionaries.

import csv
def csv_file(file_name):
    with open(file_name , 'r') as file:
        content = csv.DictReader(file)
        return list(content)


print(csv_file('csv_file.csv'))
        
