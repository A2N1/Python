import tkinter as tk
from tkinter import font

def button_click(number):
    """Fügt die gedrückte Zahl oder den Operator zum Eingabefeld hinzu."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    """Löscht das Eingabefeld."""
    entry.delete(0, tk.END)

def button_equal():
    """Berechnet das Ergebnis der eingegebenen Rechnung."""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Fehler")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefeld für die Rechnung
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Knöpfe für die Zahlen und Operatoren
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Knöpfe erstellen und im Fenster platzieren
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=button_clear)
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Fenster anzeigen
root.mainloop()
