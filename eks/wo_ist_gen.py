# Gegenstände mit Ablageort speichern (z.B. Hut Schrank).
# Ablageort für einen Gegenstand abfragen (z.B. Wo ist Hut? Schrank).
# Gegenstand und Ablageort werden in Datei gespeichert.
# Alle Gegenstände und Ablageorte anzeigen können.
# Man muss Einträge ändern und löschen können.
# Alle Gegenstände anzeigen, die an einem Ort liegen.
#

import sys
import json
import os


def lege(argumente):
    if len(argumente) != 5:
        print("Falsche Anzahl von Argumenten.")
        exit(1)

    gegenstand = argumente[2]
    ablageort = argumente[4]
    print("Ich lege", gegenstand, "in", ablageort)

    gegenstaende = dict()
    # Gegenstände laden
    if os.path.exists("gegenstaende.json"):
        try:
            gegenstaende = json.load(open("gegenstaende.json"))
        except:
            print("Fehler: Gegenstände konnten nicht geladen werden!")
            exit(1)

    # Falls der Ort nicht existiert, wird er angelegt.
    if not ablageort in gegenstaende:
        gegenstaende[ablageort] = []

    # Falls der Gegenstand schon existiert, wird er entfernt.
    for ort in gegenstaende:
        if gegenstand in gegenstaende[ort]:
            gegenstaende[ort].remove(gegenstand)

    # Gegenstand wird an den Ort gelegt.
    gegenstaende[ablageort].append(gegenstand)

    # Gegenstände speichern.
    json.dump(gegenstaende, open("gegenstaende.json", "w"))


def finde(argumente):
    if len(argumente) != 3:
        print("Falsche Anzahl von Argumenten.")
        exit(1)
    gegenstand = argumente[2]
    # Wenn die Datei nicht existiert, kann der Gegenstand nicht gesucht werden.
    if not os.path.exists("gegenstaende.json"):
        print("Keine Gegenstände vorhanden.")
        exit(0)

    # Lade Gegenstände.
    gegenstaende = dict()
    try:
        gegenstaende = json.load(open("gegenstaende.json"))
    except:
        print("Fehler: Gegenstände konnten nicht geladen werden!")
        exit(1)

    # Suche Gegenstand in allen Orten.
    for ort in gegenstaende:
        if gegenstand in gegenstaende[ort]:
            print(gegenstand, "liegt in", ort)
            exit(0)


def entferne(argumente):
    if len(argumente) != 3:
        print("Falsche Anzahl von Argumenten.")
        exit(1)
    gegenstand = argumente[2]
    # Wenn die Datei nicht existiert
    # kann der Gegenstand nicht entfernt werden.
    if not os.path.exists("gegenstaende.json"):
        print("Keine Gegenstände vorhanden.")
        exit(0)

    # Lade Gegenstand.
    gegenstaende = dict()
    try:
        gegenstaende = json.load(open("gegenstaende.json"))
    except:
        print("Fehler: Gegenstände konnten nicht geladen werden!")
        exit(1)

    # Falls der Gegenstand schon existiert, wird er entfernt.
    for ort in gegenstaende:
        if gegenstand in gegenstaende[ort]:
            gegenstaende[ort].remove(gegenstand)
            print("Gegenstand entfernt.")
            json.dump(gegenstaende, open("gegenstaende.json", "w"))
            exit(0)

    print("Gegenstand ist nicht vorhanden.")
    exit(0)


argumente = sys.argv

if len(argumente) == 1:  # Fehler, kein Befehl angegeben.
    print("Fehler: Gib einen Befehl an.")
else:
    befehl = argumente[1]
    if befehl == "lege":  # lege <Gegenstand> in <Ablageort>
        lege(argumente)
    elif befehl == "finde":  # finde <Gegenstand>
        finde(argumente)
    elif befehl == "entferne":  # entferne <Gegenstand>
        entferne(argumente)
    else:
        print("Befehl unbekannt!")
