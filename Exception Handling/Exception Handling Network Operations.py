##Write a function that attempts to open a URL and read its contents. Use try, except, and finally blocks to handle network-related errors and print an appropriate message.

import requests

def network(link):
    try:
       response = requests.get(link)
       response.raise_for_status()
       return response.text
    except requests.RequestException as e:
        print (e)
        return None
    finally:
        print("Program Executed")

print(network('www.google.com'))

