# File Operations

### Text File -

- Syntax - with open ( ‘file_name’ , ‘r or w’) as file:
- ‘w’ completely erases the previous content and overwrites.
- ‘a’ append is used to add new context to existing file.
- ‘w+’ mode is both read and write mode. The previous content is overwritten if file doesn’t exists, new file is created.
- When we need to read move the cursor back to the first line using file.seek(0), if not done then nothing is printed as cursor is at a new line which is getting printed not form the start.

### Binary File -

- Syntax for binary text - b ‘binary’
- to read and write, we use ‘wb’ or ‘rb’

### Key Takeaways -

- CSV file uses reader for reading lists and DictReader for dictionary format. In CSV the content is not stored in the memory when file is read
- JSON file reads content in dictionary by default
