my_list = [True, False, 1, "", [1, 2, 3], "hallo", -1, []]

output = ""
for value in my_list:
    if value:
        output += str(value)

print(output)
