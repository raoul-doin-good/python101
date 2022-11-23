spielfeld = [[" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "]]


def zeige(spielfeld):
  print("|" + "|".join(str(z) for z in range(1, len(spielfeld[0]) + 1)) + "|")
  print("- - - - - - - -")
  for reihe in range(len(spielfeld)):
    print("|" + "|".join(spielfeld[reihe]) + "|")


def hole_spielzug(spielfeld):
  eingabe_ok = False
  spalte = -1
  while not eingabe_ok:
    spalte = int(input("Welche Spalte? ")) - 1
    if spalte >= 0 and spalte < 7:
      for reihe in range(-1, -7, -1):
        if spielfeld[reihe][spalte] == " ":
          eingabe_ok = True
          break
    if not eingabe_ok:
      print("Ungueltige Eingabe!")
  return spalte


def setze_spielzug(spieler, spalte, spielfeld):
  for reihe in range(-1, -7, -1):
    if spielfeld[reihe][spalte] == " ":
      spielfeld[reihe][spalte] = spieler
      break


def pruefe_sieg(spielfeld):

  for reihe in spielfeld:
    for start in range(0, 4):
      fenster = reihe[start:start + 4]
      if len(set(fenster)) == 1 and fenster[0] in ["X", "O"]:
        return True
        
  for spalte in range(len(spielfeld[0])):
    for start in range(0, 3):
      fenster = [spielfeld[reihe][spalte] for reihe in range(start, start + 4)]
      print(fenster)
      if len(set(fenster)) == 1 and fenster[0] in ["X", "O"]:
        return True


print("=== Vier Gewinnt ===")
gewonnen = False
spieler = "X"

while not gewonnen:
  zeige(spielfeld)
  print(f"{spieler} ist am Zug.")
  spalte = hole_spielzug(spielfeld)
  setze_spielzug(spieler, spalte, spielfeld)
  gewonnen = pruefe_sieg(spielfeld)
  if gewonnen:
    print(f"Spieler {spieler} gewinnt:")

  if spieler == "X":
    spieler = "O"
  elif spieler == "O":
    spieler = "X"

zeige(spielfeld)