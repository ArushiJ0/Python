##Write code that attempts to import a non-existent function from `mypackage` and gracefully handles the import error by printing an error message.

try:
    from MyPackage import subtraction
except ImportError as e:
    print(f'Import error occured {e}')
    
