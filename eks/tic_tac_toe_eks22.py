# Spielablauf:
# - 1) Spielfeld anzeigen - OK
# - 2) Aktuellen Spieler anzeigen - OK
# - 3) Spieler waehlt Feld aus - OK
# - 4) Prüfen, ob das Spiel vorbei ist
#   - wenn ja: Gewinner anzeigen und Spielfeld anzeigen
#   - wenn nein: zurueck zu 1)

import random

feld01 = "1"
feld02 = "2"
feld03 = "3"
feld04 = "4"
feld05 = "5"
feld06 = "6"
feld07 = "7"
feld08 = "8"
feld09 = "9"


def reihe1():
    global feld01, feld02, feld03
    return [feld01, feld02, feld03]


def reihe2():
    global feld04, feld05, feld06
    return [feld04, feld05, feld06]


def reihe3():
    global feld07, feld08, feld09
    return [feld07, feld08, feld09]


def spalte1():
    global feld01, feld04, feld07
    return [feld01, feld04, feld07]


def spalte2():
    global feld02, feld05, feld08
    return [feld02, feld05, feld08]


def spalte3():
    global feld03, feld06, feld09
    return [feld03, feld06, feld09]


def diagonale1():
    global feld01, feld05, feld09
    return [feld01, feld05, feld09]


def diagonale2():
    global feld03, feld05, feld07
    return [feld03, feld05, feld07]


def alle_dreier():
    return [reihe1(), reihe2(), reihe3(), spalte1(), spalte2(), spalte3(), diagonale1(), diagonale2()]


def select_single_field_or_none(fields, player):
    if fields[0] == player and fields[1] == player:
        return fields[2]
    if fields[1] == player and fields[2] == player:
        return fields[0]
    if fields[0] == player and fields[2] == player:
        return fields[1]
    return None


def felder_belegt():
    global feld01, feld02, feld03, feld04, feld05, feld06, feld07, feld08, feld09
    return feld01 != "1" and feld02 != "2" and feld03 != "3" and \
        feld04 != "4" and feld05 != "5" and feld06 != "6" and \
        feld07 != "7" and feld08 != "8" and feld09 != "9"


def gewonnen():
    global feld01, feld02, feld03, feld04, feld05, feld06, feld07, feld08, feld09
    # pruefe erste Zeile:
    if feld01 == feld02 and feld02 == feld03:
        return True

    # pruefe zweite Zeile:
    if feld04 == feld05 and feld05 == feld06:
        return True

    # pruefe dritte Zeile:
    if feld07 == feld08 and feld08 == feld09:
        return True

    # pruefe erste Spalte:
    if feld01 == feld04 and feld04 == feld07:
        return True

    # pruefe zweite Spalte:
    if feld02 == feld05 and feld05 == feld08:
        return True

    # pruefe dritte Spalte:
    if feld03 == feld06 and feld06 == feld09:
        return True

    # pruefe Diagonale von links oben nach rechts unten:
    if feld01 == feld05 and feld05 == feld09:
        return True

    # pruefe Diagonale von links unten nach rechts oben:
    if feld03 == feld05 and feld05 == feld07:
        return True

    return False


def gebe_aktuellen_spieler_aus(aktueller_spieler):
    print("Spieler", aktueller_spieler, "ist dran.")


def gebe_spielfeld_aus():
    print(feld01, "|", feld02, "|", feld03)
    print(feld04, "|", feld05, "|", feld06)
    print(feld07, "|", feld08, "|", feld09)


def spielzug():
    global feld01, feld02, feld03, feld04, feld05, feld06, feld07, feld08, feld09
    feld_auswahl = input("Bitte Feld auswaehlen (1-9): ")
    auswahl_ok = False
    if feld_auswahl == "1":
        if feld01 == "1":
            feld01 = spieler
            auswahl_ok = True
    if feld_auswahl == "2":
        if feld02 == "2":
            feld02 = spieler
            auswahl_ok = True
    if feld_auswahl == "3":
        if feld03 == "3":
            feld03 = spieler
            auswahl_ok = True
    if feld_auswahl == "4":
        if feld04 == "4":
            feld04 = spieler
            auswahl_ok = True
    if feld_auswahl == "5":
        if feld05 == "5":
            feld05 = spieler
            auswahl_ok = True
    if feld_auswahl == "6":
        if feld06 == "6":
            feld06 = spieler
            auswahl_ok = True
    if feld_auswahl == "7":
        if feld07 == "7":
            feld07 = spieler
            auswahl_ok = True
    if feld_auswahl == "8":
        if feld08 == "8":
            feld08 = spieler
            auswahl_ok = True
    if feld_auswahl == "9":
        if feld09 == "9":
            feld09 = spieler
            auswahl_ok = True


def ki_auswahl():
    global feld01, feld02, feld03, feld04, feld05, feld06, feld07, feld08, feld09
    freie_felder = []
    if feld01 == "1":
        freie_felder.append(feld01)
    if feld02 == "2":
        freie_felder.append(feld02)
    if feld03 == "3":
        freie_felder.append(feld03)
    if feld04 == "4":
        freie_felder.append(feld04)
    if feld05 == "5":
        freie_felder.append(feld05)
    if feld06 == "6":
        freie_felder.append(feld06)
    if feld07 == "7":
        freie_felder.append(feld07)
    if feld08 == "8":
        freie_felder.append(feld08)
    if feld09 == "9":
        freie_felder.append(feld09)


spieler = random.choice(["X", "O"])
print(alle_dreier())
spiel_vorbei = False
while not spiel_vorbei:
    gebe_spielfeld_aus()
    gebe_aktuellen_spieler_aus(spieler)
    if spieler == "X":
        auswahl_ok = spielzug()
    else:
        ki_auswahl()

    if gewonnen():
        print(spieler, "hat gewonnen!")
        spiel_vorbei = True
    elif felder_belegt():
        print("Untentschieden.")
        spiel_vorbei = True
    if spieler == "X":
        spieler = "O"
    else:
        spieler = "X"
gebe_spielfeld_aus()
