import random  # Importiert das Modul 'random' für zufällige Auswahlmöglichkeiten

def spiel_auswahl():
    """
    Fragt den Benutzer nach seiner Wahl (Stein, Papier oder Schere) und gibt die gültige Wahl zurück.
    Die Eingabe wird in Kleinbuchstaben umgewandelt, um die Überprüfung zu vereinfachen.
    """
    while True:  # Endlosschleife, bis eine gültige Eingabe erfolgt
        benutzer_wahl = input("Wähle: Stein (s), Papier (p) oder Schere (c): ").lower()
        if benutzer_wahl in ["s", "p", "c"]:  # Überprüft, ob die Eingabe gültig ist
            return benutzer_wahl
        print("Ungültige Eingabe. Bitte wähle 's', 'p' oder 'c'.")

def computer_wahl():
    """
    Generiert eine zufällige Wahl für den Computer.
    Die Optionen sind 's' (Stein), 'p' (Papier) und 'c' (Schere).
    """
    optionen = ["s", "p", "c"]
    return random.choice(optionen)  # Wählt zufällig eine Option aus der Liste

def gewinner_ermitteln(benutzer, computer):
    """
    Ermittelt den Gewinner einer Runde basierend auf den Regeln von Scheere, Stein, Papier.
    - 's' (Stein) schlägt 'c' (Schere)
    - 'p' (Papier) schlägt 's' (Stein)
    - 'c' (Schere) schlägt 'p' (Papier)
    Gibt 'benutzer', 'computer' oder 'unentschieden' zurück.
    """
    if benutzer == computer:
        return "unentschieden"
    elif (benutzer == "s" and computer == "c") or \
         (benutzer == "p" and computer == "s") or \
         (benutzer == "c" and computer == "p"):
        return "benutzer"
    else:
        return "computer"

def spiel():
    """
    Hauptfunktion für das Spiel "Scheere, Stein, Papier".
    Das Spiel läuft, bis entweder der Benutzer oder der Computer 3 Runden gewonnen hat.
    """
    print("Willkommen zu Scheere, Stein, Papier! Gewinne 3 Runden, um das Spiel zu gewinnen.")

    benutzer_punkte = 0  # Zähler für die Punkte des Benutzers
    computer_punkte = 0  # Zähler für die Punkte des Computers

    # Hauptspielschleife: Läuft, bis einer der Spieler 3 Punkte erreicht
    while benutzer_punkte < 3 and computer_punkte < 3:
        print(f"\nAktueller Stand: Du {benutzer_punkte} - {computer_punkte} Computer")
        benutzer = spiel_auswahl()  # Benutzer gibt seine Wahl ein
        computer = computer_wahl()   # Computer wählt zufällig

        print(f"\nDeine Wahl: {benutzer}")
        print(f"Computer-Wahl: {computer}")

        ergebnis = gewinner_ermitteln(benutzer, computer)  # Ermittelt den Gewinner der Runde

        # Aktualisiert die Punkte basierend auf dem Ergebnis
        if ergebnis == "benutzer":
            benutzer_punkte += 1
            print("Du gewinnst diese Runde!")
        elif ergebnis == "computer":
            computer_punkte += 1
            print("Computer gewinnt diese Runde!")
        else:
            print("Unentschieden!")

    # Gibt den Endstand und den Gewinner des Spiels aus
    print(f"\nEndstand: Du {benutzer_punkte} - {computer_punkte} Computer")
    if benutzer_punkte == 3:
        print("Glückwunsch, Nirooo! Du hast das Spiel gewonnen! 🎉")
    else:
        print("Der Computer hat das Spiel gewonnen. Versuche es nochmal!")

# Startet das Spiel, wenn das Skript ausgeführt wird
spiel()
