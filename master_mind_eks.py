# Konzept Mastermind
# ------------------
# 1) Zahlen ausdenken
# 2) Runde ausgeben - OK
# 3) Zahlen eingeben - OK
# 4) Für jede Zahl prüfen:
#    - Ist die Zahl enthalten? - OK
#    - Ist die Position korrekt? - OK
# 5) Sind alle Zahlen korrekt?
#    - ja -> Ausgabe + Ende
#    - nein -> Ausgabe + zurück zu 2)

def give_random_number():
    return "1234"


random_number = give_random_number()
round = 1
won = False
while not won:
    won = True
    print("Current round: ", round)
    answer = input("Enter your guess: ")
    answer_position = 0
    for number in answer:
        is_contained = False
        right_position = False
        random_number_position = 0

        for number2 in random_number:

            if number == number2:
                is_contained = True
                if answer_position == random_number_position:
                    right_position = True

            random_number_position += 1
        answer_position += 1

        if is_contained == False or right_position == False:
            won = False

        print(number, " is_contained = ", is_contained)
        print(number, " right_position = ", right_position)

print("You won!")
