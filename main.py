from datetime import datetime, timedelta
import time
import keyboard  # Pour gérer les appuis de touches

current = None
is_paused = False  # Variable pour contrôler la pause

def current_time():
    global current
    current = datetime.now().strftime("%H:%M:%S")
    print(current, end="\r")

def set_time():
    user_input = input("Donner une heure (format HH:MM:SS) : ")
    try:
        custom_time = datetime.strptime(user_input, "%H:%M:%S")
        return custom_time
    except ValueError:
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")
        return None

def set_alarm_and_format():
    yes_or_no = input("Configurer une alarme ? o/n: ")
    alarm = None
    if yes_or_no == "o":
        user_alarm_input = input("Donner une heure pour l'alarme (format HH:MM:SS) : ")
        try:
            alarm = datetime.strptime(user_alarm_input, "%H:%M:%S")
        except ValueError:
            print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")
    if alarm:
        print("Une alarme a été programmée pour", alarm.strftime("%H:%M:%S"))
    return alarm  # Assurez-vous de renvoyer l'objet datetime, pas un tuple ou autre type

def counting():
    mode = int(input("1. Heure actuelle\n2. Heure spécifiée :\n"))
    alarm = set_alarm_and_format()
    
    if mode == 1:
        while True:
            if is_paused == False:
                current_time()
                if current== alarm.strftime("%H:%M:%S"):
                    print("\n===== ALARME ! =====")
                time.sleep(1)
                    
            else:
                print("\nHorloge en pause...")
            
    elif mode == 2:
        custom_time = set_time()
        if custom_time:
            while True:  
                if is_paused == False:
                    custom_time += timedelta(seconds=1)
                    print(custom_time.strftime("%H:%M:%S"), end="\r")
                    if alarm and custom_time.strftime("%H:%M:%S") == alarm.strftime("%H:%M:%S"):
                        print("\n===== ALARME ! =====")
                    time.sleep(1)
                    
                        
                else:
                    print("\nHorloge en pause...")
                
    else:
        print("Mauvaise entrée")


counting()