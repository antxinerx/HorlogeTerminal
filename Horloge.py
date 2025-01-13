from datetime import datetime ,  timedelta
import time
import keyboard

current = None
is_paused = False


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
    yes_or_no = input("Configurer une alarme ? o/n")
    if yes_or_no == "o":
        user_alarm_input = input("Donner une heure pour l'alarme (format HH:MM:SS) : ")
        try:
            alarm = datetime.strptime(user_alarm_input, "%H:%M:%S") 
            return alarm, print("Une alarme a était programmée pour", alarm.strftime("%H:%M:%S"))
        except ValueError:
                print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")
    print("Une alarme a était programmée pour",alarm.strftime("%H:%M:%S") )

def counting():
    mode = int(input("1. Heure actuelle\n2. Heure spécifiée :\n"))
    alarm = set_alarm_and_format()
    if mode == 1 : 
        while True :
            stop_time()
            if is_paused == False :
                current_time()
                stop_time()
                if alarm.strftime("%H:%M:%S") == current :
                    print("===== ALARME ! =====")
                time.sleep(1)
            else :
                print("Horloge en pause...")

    elif mode == 2 :
        custom_time = set_time()
        while True :
                stop_time()
                if is_paused == False :
                    custom_time += timedelta(seconds= 1)
                    print(custom_time.strftime("%H:%M:%S"), end = "\r")
                    if alarm == custom_time:
                        print("===== ALARME ! =====")
                    time.sleep(1)
                else : 
                     print("Horloge en pause...")
                     
    else :
        print("Mauvaise entrée")

def stop_time():
    global is_paused
    if keyboard.is_pressed("space"): 
        is_paused = not is_paused
        time.sleep(0.2)


counting()




