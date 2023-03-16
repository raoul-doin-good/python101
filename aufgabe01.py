# Benutzer gibt einzelne Werte ein
# Werte werden in einer Liste gespeichert, bis der Benutzer "q" eingibt.
# Jeder Wert der Liste wird einzeln ausgegeben mit seiner Position

# Beispiel:
# Eingabe (q = fertig): hallo
# Eingabe (q = fertig): 12
# Eingabe (q = fertig): 1.0
# Eingabe (q = fertig): q

# Ausgabe:
# Position 1: hallo
# Position 2: 12
# Position 3: 1.0

liste = []

eingabe = ""

while eingabe != "q":
    eingabe = input("Eingabe (q = fertig): ")
    if eingabe != "q":
        liste.append(eingabe)

print("Ausgabe:")
position = 1
for wert in liste:
    print("Position ", position, ": ", wert)
    position += 1
