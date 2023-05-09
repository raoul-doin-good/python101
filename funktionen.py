# Eigene Funktionen definieren

def plus(wert1, wert2):
    ergebnis = wert1 + wert2
    if ergebnis > 10:
        return wert1


def mittelwert(werte):
    summe = 0
    for wert in werte:
        summe += wert
    return summe / len(werte)

    # [1, 2, 1]
    #
    #
    # (1 + 2 + 1) / 3


print(mittelwert([1]))
print(mittelwert([0]))
print(mittelwert([0, 1]))
print(mittelwert([0, 1, -1]))
print(mittelwert([0, 1, -11, 35, 3]))
