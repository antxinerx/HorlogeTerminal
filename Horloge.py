import datetime
import time

current = None

def current_time():
    current = datetime.datetime.now().strftime("%H:%M:%S")
    print(current, end = "\r")

#def set_time(current):

def counting():
    mode = int(input("1. Heure actuelle\n2. Heure spécifiée :\n "))
    if mode == 1 : 
        while True :
            current_time()
            time.sleep(1)
    elif mode == 2 :
        while True :
            set_time()
            time.sleep(1)
    else :
        print("Mauvaise entrée")

counting()

    




