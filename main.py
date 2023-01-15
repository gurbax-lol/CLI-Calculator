from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "x" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  continue_calculations = True
  num1 = float(input("What's the first number?: "))
  
  while continue_calculations:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}.")
    continue_choice = input(f"Type 'y' to continue calculating with {answer}.\nType 'n' to start calculating with a new number. y/n : ")
    if continue_choice == "y":
      num1 = answer
    else:
      continue_calculations = False
      calculator()

calculator()
