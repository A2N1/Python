def taschenrechner():
    print("Willkommen beim Taschenrechner!")
    print("Wähle eine Operation:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")

    operation = input("Gib die Nummer der gewünschten Operation ein (1/2/3/4): ")

    try:
        zahl1 = float(input("Gib die erste Zahl ein: "))
        zahl2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
        return

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
        if zahl2 == 0:
            print("Fehler: Division durch Null ist nicht erlaubt.")
        else:
            ergebnis = zahl1 / zahl2
            print(f"Ergebnis: {zahl1} / {zahl2} = {ergebnis}")
    else:
        print("Ungültige Operation. Bitte wähle eine gültige Option.")

# Taschenrechner starten
taschenrechner()
