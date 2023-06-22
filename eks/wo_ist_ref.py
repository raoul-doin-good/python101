import sys
import json
import os


def lege(gegenstand, ort):
    gegenstaende = dict()
    if os.path.exists("gegenstaende.json"):
        gegenstaende = json.load(open("gegenstaende.json"))

    if not ort in gegenstaende:
        print(f"Neuer Ablageort: {ort}")
        gegenstaende[ort] = []

    if gegenstand in gegenstaende[ort]:
        print(f"{gegenstand} is bereits in {ort}.")
        exit(0)

    for ablageort in gegenstaende:
        if gegenstand in gegenstaende[ablageort]:
            print(f"Entferne {gegenstand} aus {ablageort}.")
            gegenstaende[ablageort].remove(gegenstand)

    if not gegenstand in gegenstaende[ort]:
        print(f"Ich lege {gegenstand} in {ort}.")
        gegenstaende[ort].append(gegenstand)
    else:
        print(f"{gegenstand} ist bereits in {ort}.")

    json.dump(gegenstaende, open("gegenstaende.json", "w"))
    exit(0)


def finde(gegenstand):
    if not os.path.exists("gegenstaende.json"):
        print(f"{gegenstand} wurde nicht gefunden.")
        exit(1)

    gegenstaende = json.load(open("gegenstaende.json"))
    for ablageort in gegenstaende:
        if gegenstand in gegenstaende[ablageort]:
            print(f"{gegenstand} liegt in {ablageort}.")
            exit(0)
    print(f"{gegenstand} wurde nicht gefunden.")
    exit(1)


def zeige_hilfe():
    print("Gib einen der folgenden Befehle ein:\n"
          "\tlege <Gegenstand> in <Ablageort>\n"
          "\tfinde <Gegenstand>\n"
          "\tzeige alles\n"
          "\tzeige <Ablageort>\n"
          "\tentferne <Gegenstand>\n"
          "\tleere <Ablageort>\n"
          )


def zeige(ort):
    if not os.path.exists("gegenstaende.json"):
        print(f"{ort} wurde nicht gefunden.")
        exit(1)

    gegenstaende = json.load(open("gegenstaende.json"))
    if not ort in gegenstaende:
        print(f"{ort} wurde nicht gefunden.")
        exit(1)

    print(f"{ort}:")
    for gegenstand in gegenstaende[ort]:
        print(f"- {gegenstand}")


def zeige_alles():
    if not os.path.exists("gegenstaende.json"):
        print(f"Es wurden keine Gegenstände abgelegt.")
        exit(0)

    gegenstaende = json.load(open("gegenstaende.json"))
    for ort in gegenstaende:
        print(f"{ort}:")
        for gegenstand in gegenstaende[ort]:
            print(f"- {gegenstand}")
    exit(0)


if len(sys.argv) == 1:
    zeige_hilfe()
else:
    befehl = sys.argv[1]
    argumente = sys.argv[2:]
    if befehl == "lege":
        gegenstand = argumente[0]
        ort = argumente[2]
        lege(gegenstand, ort)
    elif befehl == "finde":
        gegenstand = argumente[0]
        finde(gegenstand)
    elif befehl == "zeige":
        ort = argumente[0]
        if ort == "alles":
            zeige_alles()
        else:
            zeige(ort)
