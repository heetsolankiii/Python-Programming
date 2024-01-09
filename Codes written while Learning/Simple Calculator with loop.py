print("--x--SIMPLE CALCULATOR--x--\n")
start = int(input("To START enter 1: "))    # Starting point of the program
while(start == 1):
  a = int(input("Enter the first number: "))  # Accepting first number
  b = int(input("Enter the second number: "))  # Accepting second number
  print("Enter which operation would you like to perform?")  # Accepting operation
  print("\'1\' for Addition")
  print("\'2\' for Subtraction")
  print("\'3\' for Multiplication")
  print("\'4\' for Division")
  print("\'5\' for Modulus")
  operation = int(input("Enter the operation: "))
  match operation:
      case 1:
          print(a, "+", b, "=", a + b)  # Addition
      case 2:
          print(a, "-", b, "=", a - b)  # Subtraction
      case 3:
          print(a, "*", b, "=", a * b)  # Multiplication
      case 4 if b == 0:
          print("Cannot divide by zero")  # If the number is zero
      case 4:
          print(a, "/", b, "=", a / b)  # If the number is non-zero
      case 5:
          print(a, "%", b, "=", a % b)  # Modulus
      case _:
          print("Invalid operation")  # Invalid Operaion
  start = int(input("To CONTINUE enter \'1\', to STOP enter \'0\': "))  # To continue/stop the program
else:
  print("\n--x--Thank you for using the calculator.--x--")