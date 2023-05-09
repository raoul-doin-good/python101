import sys

if len(sys.argv) == 1:
    print("Gib einen der folgenden Befehle ein:\n"
          "\tlege <Gegenstand> in <Ablageort>\n"
          "\tfinde <Gegenstand>\n"
          "\tzeige alles\n"
          "\tzeige <Ablageort>\n"
          "\tentferne <Gegenstand>\n"
          "\tleere <Ablageort>\n"
          )
else:
    befehl = sys.argv[1]
    argumente = sys.argv[2:]
    if befehl == "lege":
        gegenstand = argumente[0]
        ort = argumente[2]
        print(f"Ich lege {gegenstand} in {ort}.")
