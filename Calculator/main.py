from art import logo

#Add 
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add ,
  "-" : substract ,
  "*" : multiply ,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)

  operation_symbol = input("Pick an operation from the line above: ")
  num2 = int(input("What's the second number?: "))
  calculate = operations[operation_symbol]
  first_answer = calculate(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")

  continues = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ")
  if continues == 'n':
    continues = False
    calculator()
  if continues == 'y':
    continues = True
  
  while continues:
    operation_symbol = input("Pick another operation: ")
    another_num = float(input("What's the next number?: "))
    calculate = operations[operation_symbol]
    last_answer = calculate(first_answer, another_num)
    print(f"{first_answer} {operation_symbol} {another_num} = {last_answer}")
    continues = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ")
    if continues == 'n':
      continues = False
      calculator()

calculator()
