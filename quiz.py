import random

fragen = [("Welches Jahr haben wir?", "2022"),
          ("Wann ist Weihnachten?", "24. Dezember")]

punkte = 0
while len(fragen) > 0:
  frage, richtige_antwort = random.choice(fragen)
  fragen.remove((frage, richtige_antwort))
  print(frage)
  deine_antwort = input("Antwort: ")
  if deine_antwort == richtige_antwort:
    print("Richtig!")
    punkte += 1
  else:
    print(f"Falsch! Richtige Antwort: {richtige_antwort}")

print(f"Spielende! Deine Punkte: {punkte}")
