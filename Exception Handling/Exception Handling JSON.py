##Write a function that attempts to parse a JSON string. Use try, except, and finally blocks to handle JSONDecodeError if the string is not a valid JSON and print an appropriate message.

import json
def json_file(text):
    try:
        content = json.loads(text)
        return content
    except json.JSONDecodeError as e:
        print (e)
        return None
    finally:
        print("Program Executed")

print(json_file('{"a":1,"b":2}'))
print(json_file('terry'))
