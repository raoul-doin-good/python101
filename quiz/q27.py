my_list = ["one", "two", "three"]
my_list += ["nine", "eight", "seven"]

output = ""
for word in my_list:
    if len(word) <= 4:
        output += word

print(output)
