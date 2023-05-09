# Gegenstände mit Ablageort speichern (z.B. Hut Schrank).
# Ablageort für einen Gegenstand abfragen (z.B. Wo ist Hut? Schrank).
# Gegenstand und Ablageort werden in Datei gespeichert.
# Alle Gegenstände und Ablageorte anzeigen können.
# Man muss Einträge ändern und löschen können.
# Alle Gegenstände anzeigen, die an einem Ort liegen.
#

import sys

argumente = sys.argv

if len(argumente) == 1:  # Fehler, kein Befehl angegeben.
    print("Fehler: Gib einen Befehl an.")
else:
    befehl = argumente[1]
    if befehl == "lege":  # lege <Gegenstand> in <Ablageort>
        gegenstand = argumente[2]
        ablageort = argumente[4]
        print("Ich lege", gegenstand, "in", ablageort)

        speicher_datei = open("gegenstaende.txt", "r")
        alle_ablageorte = speicher_datei.readlines()
        speicher_datei.close()

        ablageort_existiert = False
        neue_ablageorte = []
        for ort in alle_ablageorte:
            if ort.split(":")[0] == ablageort:
                neue_ablageorte.append(
                    ort.replace("\n", "") + " " + gegenstand + "\n")
                ablageort_existiert = True
            else:
                neue_ablageorte.append(ort)

        if not ablageort_existiert:
            neue_ablageorte.append(ablageort + ":" + gegenstand)

        speicher_datei = open("gegenstaende.txt", "w")
        speicher_datei.writelines(neue_ablageorte)
        speicher_datei.close()
