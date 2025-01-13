from datetime import datetime, timedelta
import time
import keyboard
import os

# --- Variables globales ---
current = None
is_paused = False
alarm = None
format_am_pm = False
# --- Fonctions ---

def current_time():

    global current
    if format_am_pm:
        current = datetime.now().strftime("%I:%M:%S %p")
    else:
        current = datetime.now().strftime("%H:%M:%S")
    print(current, end="\r")

def set_time():

    while True:
        try:
            user_input = input("Donner une heure (format HH:MM:SS) : ")
            custom_time = datetime.strptime(user_input, "%H:%M:%S").time()
            return custom_time
        except ValueError:
            print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")
        except KeyboardInterrupt:
            print('\nRetour au menu principal.')
            return None

def set_alarm_and_format():

    global alarm
    while True:
        try:
            user_alarm_input = input(
                "Donner une heure pour l'alarme (format HH:MM:SS), ou appuyez sur Entrée pour aucune alarme: "
            )
            if user_alarm_input == "":
                alarm = None
                return
            alarm = datetime.strptime(user_alarm_input, "%H:%M:%S").time()
            print("Une alarme a été programmée pour", alarm.strftime("%H:%M:%S"))
            return
        except ValueError:
            print(
                "Format invalide. Veuillez entrer l'heure au format HH:MM:SS ou appuyez sur Entrée pour aucune alarme."
            )
        except KeyboardInterrupt:
            print("\nRetour au menu principal.")
            return

def alarm_clock(mode):
    global is_paused, alarm
    if mode == 1:
        while True:
            stop_time()
            if not is_paused:
                current_time()
                if alarm and current == alarm.strftime(
                    "%I:%M:%S %p" if format_am_pm else "%H:%M:%S"
                ):
                    print("===== ALARME ! =====")
                    alarm = None
                    break
                time.sleep(1)
            else:
                print("Horloge en pause...", end="\r")
    elif mode == 2:
        custom_time = set_time()
        if custom_time is None:
            return
        current_datetime = datetime.combine(datetime.today(), custom_time)
        while True:
            stop_time()
            if not is_paused:
                current_datetime += timedelta(seconds=1)
                print(
                    current_datetime.strftime(
                        "%I:%M:%S %p" if format_am_pm else "%H:%M:%S"
                    ),
                    end="\r",
                )
                if alarm and current_datetime.time() == alarm:
                    print("===== ALARME ! =====")
                    alarm = None
                    break
                time.sleep(1)
            else:
                print("Horloge en pause...", end="\r")

def stop_time():
  
    global is_paused
    if keyboard.is_pressed("space"):
        is_paused = not is_paused
        time.sleep(0.2)
    if keyboard.is_pressed("ctrl+c"):
        raise KeyboardInterrupt

def toggle_am_pm():
   
    global format_am_pm
    format_am_pm = not format_am_pm
    print("Format AM/PM :", "Activé" if format_am_pm else "Désactivé")

# --- Boucle principale du programme ---
while True:
    try:
        os.system("cls" if os.name == "nt" else "clear")
        mode = int(
            input(
                "Choisir un mode : \n 1. Afficher l'heure actuelle \n 2. Régler l'heure \n 3. Régler l'alarme \n 4. Changer le format (AM/PM) \n Votre choix :  "
            )
        )
        if mode in [1, 2, 3]:
            if mode == 3:
                set_alarm_and_format()
            else:
                alarm_clock(mode)
        elif mode == 4:
            toggle_am_pm()
        else:
            print("Mauvaise entrée.")
    except KeyboardInterrupt:
        print("\nRetour au menu principal.")
