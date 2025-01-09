import datetime
import time

def current_time():
    current = datetime.datetime.now().strftime("%H:%M:%S")
    print(current, end = "\r")

def counting():
    while True :
        display_time()
        time.sleep(1)

counting()