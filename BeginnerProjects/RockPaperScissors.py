import random

def spiel_auswahl():
    """Fragt den Benutzer nach seiner Wahl und gibt sie zurück."""
    while True:
        benutzer_wahl = input("Wähle: Stein (s), Papier (p) oder Schere (c): ").lower()
        if benutzer_wahl in ["s", "p", "c"]:
            return benutzer_wahl
        print("Ungültige Eingabe. Bitte wähle 's', 'p' oder 'c'.")

def computer_wahl():
    """Generiert eine zufällige Wahl für den Computer."""
    optionen = ["s", "p", "c"]
    return random.choice(optionen)

def gewinner_ermitteln(benutzer, computer):
    """Ermittelt den Gewinner einer Runde."""
    if benutzer == computer:
        return "unentschieden"
    elif (benutzer == "s" and computer == "c") or \
         (benutzer == "p" and computer == "s") or \
         (benutzer == "c" and computer == "p"):
        return "benutzer"
    else:
        return "computer"

def spiel():
    """Hauptfunktion für das Spiel bis 3 Runden gewonnen sind."""
    print("Willkommen zu Scheere, Stein, Papier! Gewinne 3 Runden, um das Spiel zu gewinnen.")

    benutzer_punkte = 0
    computer_punkte = 0

    while benutzer_punkte < 3 and computer_punkte < 3:
        print(f"\nAktueller Stand: Du {benutzer_punkte} - {computer_punkte} Computer")
        benutzer = spiel_auswahl()
        computer = computer_wahl()

        print(f"\nDeine Wahl: {benutzer}")
        print(f"Computer-Wahl: {computer}")

        ergebnis = gewinner_ermitteln(benutzer, computer)

        if ergebnis == "benutzer":
            benutzer_punkte += 1
            print("Du gewinnst diese Runde!")
        elif ergebnis == "computer":
            computer_punkte += 1
            print("Computer gewinnt diese Runde!")
        else:
            print("Unentschieden!")

    print(f"\nEndstand: Du {benutzer_punkte} - {computer_punkte} Computer")
    if benutzer_punkte == 3:
        print("Glückwunsch, Nirooo! Du hast das Spiel gewonnen! 🎉")
    else:
        print("Der Computer hat das Spiel gewonnen. Versuche es nochmal!")

# Starte das Spiel
spiel()
