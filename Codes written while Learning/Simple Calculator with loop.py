def Addition(a,b):
  print(f"\n{a} + {b} = {a+b}")  # Addition

def Subtraction(a,b):
  print(f"\n{a} - {b} = {a-b}")  # Subtraction

def Multiplication(a,b):
  print(f"\n{a} * {b} = {a*b}")  # Multiplication

def Division(a,b):
  if b == 0:
    print("\nCannot divide by zero")  # If the number is zero
  else:
    print(f"\n{a} / {b} = {a/b}")  # If the number is non-zero

start = 1   # Starting point of the program
while(start == 1):
  try:
    a = int(input("Enter the first number: "))  # Accepting first number
    b = int(input("Enter the second number: "))  # Accepting second number
    print("Enter which operation would you like to perform?")  # Accepting operation
    print("\'+\' for Addition")
    print("\'-\' for Subtraction")
    print("\'*\' for Multiplication")
    print("\'/\' for Division")
    operation = (input("\nEnter the operation: "))
    match operation:
        case "+":
          Addition(a,b)
        case "-":
          Subtraction(a,b)
        case "*":
          Multiplication(a,b)
        case "/":
          Division(a,b)
        case _:
            print("\nInvalid operation")  # Invalid Operaion
  except ValueError:
    print("Please enter a valid number")
  start = int(input("\nTo CONTINUE enter \'1\', to STOP enter \'0\': "))  # To continue/stop the program
else:
  print("\n--x--Thank you for using the calculator.--x--")