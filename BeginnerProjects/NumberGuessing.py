# Number Guessing - Version 1.0
# Importiere das Modul 'random', um Zufallszahlen zu generieren
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generiere eine zufällige Zahl zwischen 1 und 100
    secret_number = random.randint(1, 100)
    # Zähler für die Anzahl der Versuche
    attempts = 0

    # Endlosschleife, bis der Benutzer die richtige Zahl errät
    while True:
        try:
            # Fordere den Benutzer auf, eine Zahl einzugeben
            guess = int(input("Take a guess: "))
            # Erhöhe den Versuchszähler
            attempts += 1

            # Überprüfe, ob die geratene Zahl kleiner als die geheime Zahl ist
            if guess < secret_number:
                print("Too low! Try again.")
            # Überprüfe, ob die geratene Zahl größer als die geheime Zahl ist
            elif guess > secret_number:
                print("Too high! Try again.")
            # Wenn die Zahl richtig geraten wurde
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                # Beende die Schleife, da das Spiel gewonnen wurde
                break
        # Falls der Benutzer keine gültige Zahl eingibt (z. B. Buchstaben)
        except ValueError:
            print("Please enter a valid number.")

# Überprüfe, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Starte das Spiel
    number_guessing_game()
