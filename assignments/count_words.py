separators = [" ", ".", ",", "!", "?"]
text = input("Enter text: ")


word_count = 0
end_separator = False
token_in_progress = False

for letter in text:
    if letter not in separators and not token_in_progress:
        token_in_progress = True

    if letter in separators:
        if token_in_progress:
            word_count += 1
            token_in_progress = False

if token_in_progress:
    word_count += 1

print(word_count)
