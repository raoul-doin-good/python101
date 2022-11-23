operation = input("Operation: ")
einzelteile = operation.split(" ")

if len(einzelteile) != 3:
  print("Fehler! Operation muss drei Teile haben (Operand1 Operator Operand2).")
  exit(1)

operations = {
  "+": lambda x,y : x + y,
  "-": lambda x,y : x - y,
  "*": lambda x,y : x * y,
  "/": lambda x,y : x / y
}
operand1 = float(einzelteile[0])
operand2 = float(einzelteile[-1])
operator = einzelteile[1]
ergebnis = operations[operator](operand1, operand2)

print(f"Ergebnis: {operand1} {operator} {operand2} = {ergebnis}")