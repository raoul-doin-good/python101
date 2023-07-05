a = True
b = False
c = False

output = ""

if a and b:
    output += "1"

if a or b:
    output += "2"

if not c:
    output += "3"

if a and (b or c):
    output += "4"

if a or b or c:
    output += "5"

print(output)
