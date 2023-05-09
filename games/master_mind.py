import random

print("=== Willkommen zu Master Mind! ===")

nochmal = True
while nochmal:
  anzahl_zahlen = int(input("Wie viele Zahlen möchtest du raten?\n"))

  zahlen = [str(random.randint(0, 9)) for i in range(anzahl_zahlen)]

  runde = 1
  gewonnen = False
  while not gewonnen:
    versuch = input(f"{runde}. Runde:\n").split(" ")
    ergebnis = [
      1 if v == z else 0 if v in zahlen else -1
      for v, z in zip(versuch, zahlen)
    ]
    gewonnen = 0 not in ergebnis and -1 not in ergebnis
    ausgabe = " ".join(
      ["X" if e == 1 else "-" if e == -1 else "O" for e in ergebnis])
    print(ausgabe)
    if gewonnen:
      print(f"Gewonnen nach {runde} Runden.")
      break
    runde += 1

  nochmal = (input("Neue Runde? (j/n): ") == "j")

print("=== Bis bald! ===")