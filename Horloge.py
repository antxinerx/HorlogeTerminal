from datetime import datetime
import time

current = None


def current_time():
    current = datetime.now().strftime("%H:%M:%S")
    print(current, end = "\r")

def set_time():
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
        set_time()
        while True :
            print(current)
            time.sleep(1)
    else :
        print("Mauvaise entrée")


counting()
    




