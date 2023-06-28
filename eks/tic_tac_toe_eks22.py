# KI:
# 1. Wenn leer, dann Spielfeld 5
#   - Alle Felder durchgehen, wenn keines davon 'X' oder 'O' ist, ist das Feld leer. - OK

# 2. Wenn ich gewinnen kann, nimm das Feld, das gewinnt.
#   - Alle Spalten, alle Reihen, alle Diagonalen überprüfen:
#        - Habe ich schon zwei Felder belegt und ist das dritte Feld noch frei?
#        - Wenn ja, nimm das noch freie Feld.

# 3. Wenn der Gegner im nächsten Zug gewinnt, nimm das Feld, das dies verhindert
#   - Alle Spalten, alle Reihen, alle Diagonalen überprüfen:
#        - Hat der Gegner schon zwei Felder belegt und ist das dritte Feld noch frei?
#        - Wenn ja, nimm das noch freie Feld.

# 4. Wähle ein zufälliges Feld.
#   - Bestimme alle Felder, die noch frei sind, wähle zufällig eines aus. - OK

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


def freie_felder():
    global feld01, feld02, feld03, feld04, feld05, feld06, feld07, feld08, feld09
    felder = [feld01, feld02, feld03, feld04,
              feld05, feld06, feld07, feld08, feld09]
    leere_felder = []
    for feld in felder:
        if feld != "X" and feld != "O":
            leere_felder.append(feld)
    return leere_felder


def finde_einzelnes_freies_feld(felder, spieler):
    anzahl = felder.count(spieler)
    if anzahl == 2:
        for feld in felder:
            if feld != spieler and feld in freie_felder():
                return feld
    return None


def ki_auswahl():
    leere_felder = freie_felder()

    # Regel 1
    if len(leere_felder) == 9:
        return "5"

    # Regel 2
    reihe1 = [feld01, feld02, feld03]
    reihe2 = [feld04, feld05, feld06]
    reihe3 = [feld07, feld08, feld09]
    spalte1 = [feld01, feld04, feld07]
    spalte2 = [feld02, feld05, feld08]
    spalte3 = [feld03, feld06, feld09]
    diagonale1 = [feld01, feld05, feld09]
    diagonale2 = [feld03, feld05, feld07]
    alle_dreier = [reihe1, reihe2, reihe3, spalte1,
                   spalte2, spalte3, diagonale1, diagonale2]

    feld_auswahl = finde_einzelnes_freies_feld(reihe1, "O")
    if feld_auswahl != None:
        return feld_auswahl

    return random.choice(leere_felder)


def ki_auswahl_ref():
    leere_felder = freie_felder()

    # Regel 1
    if len(leere_felder) == 9:
        return "5"

    if len(leere_felder) == 1:
        return leere_felder[0]

    # Regel 2
    reihe1 = [feld01, feld02, feld03]
    reihe2 = [feld04, feld05, feld06]
    reihe3 = [feld07, feld08, feld09]
    spalte1 = [feld01, feld04, feld07]
    spalte2 = [feld02, feld05, feld08]
    spalte3 = [feld03, feld06, feld09]
    diagonale1 = [feld01, feld05, feld09]
    diagonale2 = [feld03, feld05, feld07]
    alle_dreier = [reihe1, reihe2, reihe3, spalte1,
                   spalte2, spalte3, diagonale1, diagonale2]

    # Prüfe, ob KI gewinnen kann.
    for dreier in alle_dreier:
        feld_auswahl = finde_einzelnes_freies_feld(dreier, "O")
        if feld_auswahl != None:
            return feld_auswahl

    # Prüfe, ob Gegner gewinnen kann.
    for dreier in alle_dreier:
        feld_auswahl = finde_einzelnes_freies_feld(dreier, "X")
        if feld_auswahl != None:
            return feld_auswahl

    return random.choice(leere_felder)


print(finde_einzelnes_freies_feld(["3", "O", "O"], "O"))


# Spielablauf:
# - 1) Spielfeld anzeigen - OK
# - 2) Aktuellen Spieler anzeigen - OK
# - 3) Spieler waehlt Feld aus - OK
# - 4) Prüfen, ob das Spiel vorbei ist
#   - wenn ja: Gewinner anzeigen und Spielfeld anzeigen
#   - wenn nein: zurueck zu 1)
#

def felder_belegt():
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


def spieler_auswahl():
    while True:
        feld_auswahl = input("Bitte Feld auswaehlen (1-9): ")
        if feld_auswahl in freie_felder():
            return feld_auswahl
        else:
            print("Ungültige Auswahl!")


def setze_auswahl(feld_auswahl, spieler):
    global feld01, feld02, feld03, feld04, feld05, feld06, feld07, feld08, feld09
    if feld_auswahl == "1":
        if feld01 == "1":
            feld01 = spieler
    if feld_auswahl == "2":
        if feld02 == "2":
            feld02 = spieler
    if feld_auswahl == "3":
        if feld03 == "3":
            feld03 = spieler
    if feld_auswahl == "4":
        if feld04 == "4":
            feld04 = spieler
    if feld_auswahl == "5":
        if feld05 == "5":
            feld05 = spieler
    if feld_auswahl == "6":
        if feld06 == "6":
            feld06 = spieler
    if feld_auswahl == "7":
        if feld07 == "7":
            feld07 = spieler
    if feld_auswahl == "8":
        if feld08 == "8":
            feld08 = spieler
    if feld_auswahl == "9":
        if feld09 == "9":
            feld09 = spieler


spieler = random.choice(["X", "O"])
spiel_vorbei = False
while not spiel_vorbei:
    gebe_spielfeld_aus()
    gebe_aktuellen_spieler_aus(spieler)
    feld_auswahl = ""

    if spieler == "X":
        feld_auswahl = spieler_auswahl()
    else:
        feld_auswahl = ki_auswahl_ref()
        print("O waehlt:", feld_auswahl)

    setze_auswahl(feld_auswahl, spieler)

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
