from datetime import datetime ,  timedelta
import time

current = None


def current_time():
    global current 
    current = datetime.now().strftime("%H:%M:%S")
    print(current, end = "\r")

def set_time(): 
    user_input = input("Donner une heure (format HH:MM:SS) : ")
    try:
        custom_time = datetime.strptime(user_input, "%H:%M:%S")
        return custom_time
    except ValueError:
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")

    
def set_alarm_and_format():
    set_alarm
    yes_or_no = input("Configurer une alarme ? o/n")
    if yes_or_no == "o":
        alarm = input("Donner une heure (format HH:MM:SS) : ")


def counting():
    mode = int(input("1. Heure actuelle\n2. Heure spécifiée :\n"))
    if mode == 1 : 
        while True :
            current_time()
            time.sleep(1)
    elif mode == 2 :
        custom_time = set_time()
        while True :
                custom_time += timedelta(seconds= 1)
                print(custom_time.strftime("%H:%M:%S"), end = "\r")
                time.sleep(1)
    else :
        print("Mauvaise entrée")


counting()




