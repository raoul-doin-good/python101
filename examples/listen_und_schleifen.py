liste = [1, "zwei", 3.0, False] # Eine Liste kann Werte mit verschiedenen Datentypen enthalten.
print(liste[0]) # Mit dem Index kann ich auf die einzelnen Elemente zugreifen. Der Index faengt bei 0 an!
print(liste[1])
print(liste[2])
print(liste[3])

# Mit einem negativen Index kann ich auf die Elemente von hinten zugreifen:
print(liste[-1])
print(liste[-2])
print(liste[-3])
print(liste[-4])

for wert in liste: # Die for-Schleife durchlaeuft die gesamte Liste und schreibt jeweils das naechste Element in die Variable 'wert'.
  print(wert)

# Mit der Funktion len() bekomme ich die Laenge der Liste heraus
print(len(liste))

# Wenn ich versuche auf einen Index zuzugreifen, der nicht existiert, gibt es eine Fehlermeldung
print(liste[4])
