def taschenrechner():
    """
    Ein einfacher Taschenrechner, der die vier Grundrechenarten unterstützt.
    Der Benutzer kann zwischen Addition, Subtraktion, Multiplikation und Division wählen.
    Das Programm läuft in einer Schleife, bis der Benutzer es beendet.
    """
    # Begrüßung und Menü anzeigen
    print("Willkommen beim Taschenrechner!")
    print("Wähle eine Operation:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")

    # Endlosschleife, bis der Benutzer das Programm beendet
    while True:
        # Benutzereingabe für die Operation abfragen
        operation = input("Gib die Nummer der gewünschten Operation ein (1/2/3/4) oder 'e' zum Beenden: ")

        # Programm beenden, wenn der Benutzer 'e' eingibt
        if operation.lower() == 'e':
            print("Taschenrechner wird beendet.")
            break  # Schleife verlassen

        # Überprüfen, ob die Eingabe gültig ist
        if operation not in ['1', '2', '3', '4']:
            print("Ungültige Eingabe. Bitte wähle 1, 2, 3, 4 oder 'e' zum Beenden.")
            continue  # Zurück zum Anfang der Schleife

        # Zahlen vom Benutzer abfragen und in Float umwandeln
        try:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            zahl2 = float(input("Gib die zweite Zahl ein: "))
        except ValueError:
            # Fehlerbehandlung, falls keine Zahl eingegeben wurde
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
            continue  # Zurück zum Anfang der Schleife

        # Je nach gewählter Operation die Berechnung durchführen
        if operation == '1':
            ergebnis = zahl1 + zahl2
            print(f"Ergebnis: {zahl1} + {zahl2} = {ergebnis}")
        elif operation == '2':
            ergebnis = zahl1 - zahl2
            print(f"Ergebnis: {zahl1} - {zahl2} = {ergebnis}")
        elif operation == '3':
            ergebnis = zahl1 * zahl2
            print(f"Ergebnis: {zahl1} * {zahl2} = {ergebnis}")
        elif operation == '4':
            # Division durch Null verhindern
            if zahl2 == 0:
                print("Fehler: Division durch Null ist nicht erlaubt.")
            else:
                ergebnis = zahl1 / zahl2
                print(f"Ergebnis: {zahl1} / {zahl2} = {ergebnis}")

# Hauptprogramm: Taschenrechner-Funktion aufrufen
if __name__ == "__main__":
    taschenrechner()
