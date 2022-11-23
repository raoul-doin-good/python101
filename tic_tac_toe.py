import os

hoehe = 3
breite = 3
spielfeld = [zahl + 1 for zahl in range(hoehe * breite)]


def zeige(spielfeld):
  for z in range(3):
    zeile = [str(feld) for feld in spielfeld[z * 3:z * 3 + 3]]
    print("|".join(zeile))


def sieg(spielfeld):
  for l in range(3):
    if len(set(spielfeld[l * 3:l * 3 + 3])) == 1:
      return True
    if len(set(spielfeld[l:l + 7:3])) == 1:
      return True
    if spielfeld[0] == spielfeld[4] and spielfeld[4] == spielfeld[8]:
      return True
    if spielfeld[2] == spielfeld[4] and spielfeld[4] == spielfeld[6]:
      return True
  return False


def unentschieden(spielfeld):
  return all(feld in ["X", "O"] for feld in spielfeld)


def spielzug(spielfeld):
  feld_ok = False
  while not feld_ok:
    feld = int(input("Feld eingeben: "))
    if feld >= 1 and feld <= 9 and spielfeld[feld - 1] not in ["X", "O"]:
      feld_ok = True
      spielfeld[feld - 1] = "X" if spieler == 1 else "O"
    else:
      print("Feld ungueltig!")


zu_ende = False
spieler = 1

while not zu_ende:
  os.system('clear')
  print("==== Tic Tac Toe ====")

  zeige(spielfeld)
  print(f"Spieler {spieler} ist dran.")
  spielzug(spielfeld)
  if sieg(spielfeld):
    print(f"Spieler {spieler} hat gewonnen:")
    zu_ende = True
  elif unentschieden(spielfeld):
    print("Unentschieden:")
    zu_ende = True
  else:
    if spieler == 1:
      spieler = 2
    elif spieler == 2:
      spieler = 1

zeige(spielfeld)
