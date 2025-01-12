import time
from datetime import datetime
import os

def afficher_heure(heures=None, minutes=None, secondes=None, mode_12h=False):
  """Affiche l'heure avec mise à jour chaque seconde.

  Args:
    heures: Heures à afficher (optionnel).
    minutes: Minutes à afficher (optionnel).
    secondes: Secondes à afficher (optionnel).
    mode_12h: Si True, affiche l'heure au format 12h (AM/PM).
  """
  try:
    while True:
      now = datetime.now()
      if heures is not None:
        now = now.replace(hour=heures)
      if minutes is not None:
        now = now.replace(minute=minutes)
      if secondes is not None:
        now = now.replace(second=secondes)

      if mode_12h:
        heure_format = now.strftime("%I:%M:%S %p")
      else:
        heure_format = now.strftime("%H:%M:%S")
      print(heure_format, end="\r")
      time.sleep(1)
  except KeyboardInterrupt:
    print("\nAffichage de l'heure arrêté.")
    os.system('cls' if os.name == 'nt' else 'clear') # Ajout de la commande clear
    return  # Retourne à la fonction appelante

def regler_heure():
  """Demande à l'utilisateur de saisir une heure et met à jour l'affichage."""
  while True:
    try:
      heures = int(input("Heures : "))
      minutes = int(input("Minutes : "))
      secondes = int(input("Secondes : "))
      if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <= 59:
        # On passe les valeurs à afficher_heure
        afficher_heure(heures=heures, minutes=minutes, secondes=secondes)
        break
      else:
        print("Heure invalide. Veuillez entrer une heure entre 00:00:00 et 23:59:59.")
    except ValueError:
      print("Entrée invalide. Veuillez saisir des nombres entiers.")

def regler_alarme():
  """Demande à l'utilisateur de régler une heure d'alarme."""
  while True:
    try:
      h_alarme = int(input("Heure de l'alarme (heures) : "))
      m_alarme = int(input("Heure de l'alarme (minutes) : "))
      s_alarme = int(input("Heure de l'alarme (secondes) : "))
      if 0 <= h_alarme <= 23 and 0 <= m_alarme <= 59 and 0 <= s_alarme <= 59:
        break
      else:
        print("Heure invalide. Veuillez entrer une heure entre 00:00:00 et 23:59:59.")
    except ValueError:
      print("Entrée invalide. Veuillez saisir des nombres entiers.")

  while True:
    now = datetime.now()
    if now.hour == h_alarme and now.minute == m_alarme and now.second == s_alarme:
      print("ALARME ! Il est {}:{}:{} !".format(h_alarme, m_alarme, s_alarme))
      break
    time.sleep(5)

def main():
  """Affiche un menu et exécute l'option choisie."""
  while True:
    print("\n--- Menu Horloge ---")
    print("1. Afficher l'heure")
    print("2. Régler l'heure")
    print("3. Régler l'alarme")
    print("4. Quitter")

    choix = input("Choisissez une option : ")

    if choix == '1':
      mode_12h = input("Mode 12h (AM/PM) ? (o/n) : ").lower() == 'o'
      afficher_heure(mode_12h=mode_12h)
    elif choix == '2':
      regler_heure()
    elif choix == '3':
      regler_alarme()
    elif choix == '4':
      break
    else:
      print("Choix invalide. Veuillez choisir une option valide.")
    os.system('cls' if os.name == 'nt' else 'clear') # Ajout de la commande clear

if __name__ == "__main__":
  main()
