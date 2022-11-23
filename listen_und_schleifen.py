liste = [1, "zwei", 3.0, False
         ]  # Eine Liste kann Werte mit verschiedenen Datentypen enthalten.

# Mit dem Index kann ich auf die einzelnen Elemente zugreifen. Der Index faengt bei 0 an!
print(liste[0])  # Gibt das erste Element der Liste aus.
print(liste[1])  # Gibt das zweite Element der Liste aus.
print(liste[2])  # Gibt das dritte Element der Liste aus.
print(liste[3])  # Gibt das vierte Element der Liste aus

# Mit einem negativen Index kann ich auf die Elemente von hinten zugreifen:
print(liste[-1])  # Gibt das letzte Element der Liste aus.
print(liste[-2])  # Gibt das vorletzte Element der Liste aus.
print(liste[-3])  # Gibt das vorvorletzte Element der Liste aus.
print(liste[-4])  # Gibt das vorvorvorletzte Element der Liste aus.

for wert in liste:  # Die for-Schleife durchlaeuft die gesamte Liste und schreibt jeweils das naechste Element in die Variable 'wert'.
  print(wert)

# Mit der Funktion len() bekomme ich die Laenge der Liste heraus
print(len(liste))

# Wenn ich versuche auf einen Index zuzugreifen, der nicht existiert, gibt es eine Fehlermeldung
print(liste[4])
