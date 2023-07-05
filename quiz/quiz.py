import os
import sys
import glob
import importlib
import contextlib
import io
import random


def clear(): return os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        # Pass names of quiz files to run a specific questions.
        quiz_files = sys.argv[1:]
    else:
        # Normal mode: run all quiz files in this directory.
        quiz_dir = os.path.dirname(__file__)
        quiz_files = glob.glob(os.path.join(quiz_dir, "*.py"))

        # Remove this script.
        quiz_files.remove(__file__)

        # Take 10 ramdon questions.
        random.shuffle(quiz_files)
        quiz_files = quiz_files[:10]

    num_questions = len(quiz_files)
    points = 0
    wrong_answers = []
    for i, quiz_file in enumerate(quiz_files):
        file_name = os.path.basename(quiz_file)
        question_id = file_name[1:3]
        clear()
        file_content = open(quiz_file).read()
        print(f"{i + 1}. - Was gibt das folgende Programm aus?")
        print(f"Frage ID: {question_id}")
        print(f"==============================================\n")
        print(file_content)
        print(f"\n==============================================")

        answer = input("Antwort: ")
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            importlib.import_module(file_name[:-3])
        output = capture.getvalue()[:-1]  # remove trailing \n

        if output == answer:
            print("Richtig!")
            points += 1
        else:
            wrong_answers.append(question_id)
            print("Falsch!")

        if i != num_questions - 1:
            input("Drücke [Enter] für die nächste Frage.")

    print("\nSpielende!")
    print(f"Deine Punktzahl: {points} von {num_questions}.")

    if wrong_answers:
        print(f"Du hast diese Fragen falsch beantwortet: {wrong_answers}")
    else:
        print("Glückwunsch! Du hast alle Fragen richtig beantwortet!")
