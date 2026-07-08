##Use the `os` module to create a new directory, list the contents of the current directory, and remove the newly created directory.

import os
os.mkdir('directory')
print(os.listdir())
os.rmdir('directory')
print(os.listdir())
