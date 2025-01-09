from datetime import datetime
import time

current = None


def current_time():
    global current 
    current = datetime.now().strftime("%H:%M:%S")
    print(current, end = "\r")

def set_time():
    global current 
    current = input("Donner une heure (format HH:MM:SS) : ")
    try:
        current = datetime.strptime(current, "%H:%M:%S").strftime("%H:%M:%S")
    except ValueError:
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")

def counting():
    mode = int(input("1. Heure actuelle\n2. Heure spécifiée :\n"))
    if mode == 1 : 
        while True :
            current_time()
            time.sleep(1)
    elif mode == 2 :
         while current is None:  
            set_time()
         while True :
            if current is not None:
                print(current, end = "\r")
                time.sleep(1)
    else :
        print("Mauvaise entrée")


counting()




