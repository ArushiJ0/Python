##Write a function that creates a log file named `activity.log` and writes log messages with timestamps.

import datetime

def log_file(message):
    with open('activity.log' , 'a') as file:
        timestamp = datetime.datetime.now().isoformat()
        file.write(f'({timestamp}){message}\n')

log_file('New message')
        
