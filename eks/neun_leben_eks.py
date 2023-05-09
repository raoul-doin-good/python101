import random


def ist_buchstabe(eingabe):
    if len(eingabe) == 1:
        return True
    else:
        return False


def update_wort(wort, ausgabe_wort, geraten):
    neuer_status = ""
    index = 0
    for buchstabe in wort:
        if buchstabe == geraten:
            neuer_status += buchstabe
        else:
            neuer_status += ausgabe_wort[index]
        index += 1
    return neuer_status


# Ablauf
anzahl_leben = 9

# 1. Wort wählen und anzeigen
wort_datei = open("woerter.txt")
woerter = wort_datei.readlines()
wort_datei.close()
wort = random.choice(woerter)
wort = wort.replace("\n", "")

ausgabe_wort = ""
for buchstabe in wort:
    ausgabe_wort += "?"

while True:
    print("gesuchtes Wort: ", ausgabe_wort)
    print("Anzahl Leben: ", anzahl_leben)

    # 2. Input vom Spieler holen - OK
    geraten = input("Bitte Wort oder Buchstaben eingeben: ")

    # 3. Prüfen, ob Input ein Buchstabe ist - Ok
    if ist_buchstabe(geraten):
        # Dopplung
        if geraten in ausgabe_wort:
            print("Buchstabe wurde bereits erraten!")
            anzahl_leben -= 1
        # Richtiger Buchstabe
        elif geraten in wort:
            print("Buchstabe ist enthalten!")
            ausgabe_wort = update_wort(wort, ausgabe_wort, geraten)
            if ausgabe_wort == wort:
                print("Du hast das Lösungswort erraten!")
                break
        # Falscher Buchstabe
        else:
            print("Buchstabe ist nicht enthalten!")
            anzahl_leben -= 1
    # 3B. Wenn Input ein Wort ist:
    elif len(geraten) > 1:
        # Prüfen, ob das Wort korrekt ist:
        if geraten == wort:
            # Wenn ja: Gewinn ausgeben.
            print("Du hast das Lösungswort erraten!")
            break
        else:
            # Wenn nein: Fehler anzeigen, Leben abziehen
            print("Falsch geraten!")
            anzahl_leben -= 1

    # 4. Prüfen, ob Leben == 0: - ok
    if anzahl_leben == 0:
        print("Du hast keine Leben mehr!")
        print("Das Wort war: ", wort)
        break
