# Projekt: "Neun Leben"


def update_current_state(word, current_state, guess):
    new_state = ""
    index = 0
    for letter in word:
        if letter == guess:
            new_state += letter
        else:
            new_state += current_state[index]
        index += 1
    return new_state


lives = 9
word = "hallo"
unknown = "?"
current_state = unknown * len(word)

print("Willkommen zu Neun Leben! Errate das Wort:")
while True:
    print("\nAktueller Stand:", current_state)
    print("Leben:", lives)

    guess = input("Rate einen Buchstaben oder das Wort: ")

    if len(guess) == 0:
        continue

    if len(guess) == 1:
        if guess in current_state:
            print("Diesen Buchstaben hast du bereits erraten.")
            lives -= 1
        elif guess in word:
            print("Buchstabe ist enthalten.")
            current_state = update_current_state(word, current_state, guess)
        else:
            print("Buchstabe ist nicht enthalten.")
            lives -= 1

        if current_state == word:
            print("Du hast alle Buchstaben erraten! Gewonnen!")
            break
    else:
        if word == guess:
            print("Du hast das Wort erraten! Gewonnen!")
            break
        else:
            print("Falsch!")
            lives -= 1

    if lives == 0:
        print("Keine Leben mehr! Verloren!")
        break


print("gesuchtes Wort:", word)
