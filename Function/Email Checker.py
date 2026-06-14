import re
def email_checker(email):
    pattern = r'^[a-zA-Z0-9.-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    return re.match(pattern,email) is not None

print(email_checker('amm08@gmail.com'))
