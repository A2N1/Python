import random

def hangman():
    # Wortliste
    woerter = ["python", "hangman", "programmieren", "computer", "entwickler", "algorithm", "datenbank"]
    geheimwort = random.choice(woerter).lower()
    geratene_buchstaben = set()
    versuche = 6  # Anzahl der erlaubten Fehler

    # ASCII-Grafik für den Galgen
    galgen = [
        """
         ------
         |    |
              |
              |
              |
              |
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\\  |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\\  |
        /     |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\\  |
        / \\  |
              |
        """
    ]

    print("Willkommen bei Hangman!")
    print(f"Das Wort hat {len(geheimwort)} Buchstaben.")

    while versuche > 0:
        # Aktuellen Stand anzeigen
        anzeige = ""
        for buchstabe in geheimwort:
            if buchstabe in geratene_buchstaben:
                anzeige += buchstabe + " "
            else:
                anzeige += "_ "
        print(anzeige)

        # Galgen zeichnen
        print(galgen[6 - versuche])

        # Eingabe des Spielers
        raten = input("Rate einen Buchstaben: ").lower()

        if raten in geratene_buchstaben:
            print("Du hast diesen Buchstaben schon geraten!")
            continue

        geratene_buchstaben.add(raten)

        if raten in geheimwort:
            print(f"Richtig! '{raten}' ist im Wort.")
        else:
            print(f"Falsch! '{raten}' ist nicht im Wort.")
            versuche -= 1
            print(f"Du hast noch {versuche} Versuche übrig.")

        # Überprüfen, ob das Wort erraten wurde
        if all(buchstabe in geratene_buchstaben for buchstabe in geheimwort):
            print(f"Glückwunsch! Du hast das Wort '{geheimwort}' erraten!")
            break

    if versuche == 0:
        print(galgen[6])
        print(f"Game Over! Das Wort war '{geheimwort}'.")

# Spiel starten
hangman()
