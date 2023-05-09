import random

def benutzer_eingabe():
  return int(input("Dein Vorschlag: "))

def vergleiche(eingabe, ziel):
  if eingabe == ziel:
    print("Richtig!")
    return True
  elif eingabe < ziel:
    print("Zu niedrig!")
  elif eingabe > ziel:
    print("Zu hoch!")
  return False


print("=== Rate die Zahl! ===")
zahl = random.randint(1, 101)

gewonnen = False
versuche = 0

while not gewonnen:
  versuche += 1
  versuch = benutzer_eingabe()
  gewonnen = vergleiche(versuch, zahl)

print(f"Gewonnen nach {versuche} Versuchen!")
