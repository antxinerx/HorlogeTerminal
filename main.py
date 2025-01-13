from datetime import datetime, timedelta
import time
import keyboard
import os

# --- Variables globales ---
current = None  # Variable pour stocker l'heure actuelle formatée
is_paused = False  # Flag pour la pause
alarm = None  # Variable pour stocker l'heure de l'alarme
format_am_pm = False  # Flag pour l'affichage AM/PM, initialisé à False

# --- Fonctions ---

def current_time():
    """
    Fonction pour obtenir l'heure actuelle et l'afficher.
    Met à jour la variable globale 'current' avec l'heure actuelle formatée.
    Utilise le format AM/PM si 'format_am_pm' est True.
    """
    global current
    if format_am_pm:
        current = datetime.now().strftime("%I:%M:%S %p")  # Format avec AM/PM
    else:
        current = datetime.now().strftime("%H:%M:%S")  # Format 24h
    print(current, end="\r")

def set_time():
    """
    Fonction pour demander à l'utilisateur de saisir une heure.
    Valide le format de l'heure et retourne un objet datetime.time.
    En cas d'interruption clavier (Ctrl+C), retourne None.
    """
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
    """
    Fonction pour configurer l'heure de l'alarme.
    Demande à l'utilisateur de saisir une heure d'alarme valide (ou aucune).
    Met à jour la variable globale 'alarm'.
    """
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
    """
    Fonction principale pour gérer l'horloge et l'alarme.
    Prend en entrée le mode d'affichage (1 ou 2).
    Gère l'affichage de l'heure, la pause et le déclenchement de l'alarme.
    """
    global is_paused, alarm
    if mode == 1:
        while True:
            stop_time()
            if not is_paused:
                current_time()
                if alarm and current == alarm.strftime(
                    "%I:%M:%S %p" if format_am_pm else "%H:%M:%S"
                ):  # Utilise le format AM/PM si nécessaire
                    print("===== ALARME ! =====")
                    alarm = None  # Reset alarm after it rings
                    break
                time.sleep(1)
            else:
                print("Horloge en pause...", end="\r")
    elif mode == 2:
        custom_time = set_time()
        if custom_time is None:  # Vérifier si set_time() a été interrompu
            return  # Retourner au menu principal si interrompu
        current_datetime = datetime.combine(datetime.today(), custom_time)
        while True:
            stop_time()
            if not is_paused:
                current_datetime += timedelta(seconds=1)
                print(
                    current_datetime.strftime(
                        "%I:%M:%S %p" if format_am_pm else "%H:%M:%S"
                    ),  # Utilise le format AM/PM si nécessaire
                    end="\r",
                )
                if alarm and current_datetime.time() == alarm:
                    print("===== ALARME ! =====")
                    alarm = None  # Reset alarm after it rings
                    break
                time.sleep(1)
            else:
                print("Horloge en pause...", end="\r")

def stop_time():
    """
    Fonction pour gérer la pause et la reprise de l'horloge avec la barre espace.
    Gère également l'interruption clavier avec Ctrl+C.
    """
    global is_paused
    if keyboard.is_pressed("space"):
        is_paused = not is_paused
        time.sleep(0.2)
    if keyboard.is_pressed("ctrl+c"):
        raise KeyboardInterrupt

def toggle_am_pm():
    """
    Fonction pour activer/désactiver l'affichage AM/PM.
    Modifie la variable globale 'format_am_pm'.
    """
    global format_am_pm
    format_am_pm = not format_am_pm
    print("Format AM/PM :", "Activé" if format_am_pm else "Désactivé")

# --- Boucle principale du programme ---
while True:
    try:
        os.system("cls" if os.name == "nt" else "clear")  # Nettoyage du terminal
        mode = int(
            input(
                "1. Afficher l'heure actuelle\n2. Heure spécifiée\n3. Régler l'alarme\n4. Format AM/PM\nChoisissez une option : "
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
