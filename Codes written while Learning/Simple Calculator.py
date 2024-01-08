a = int(input("Enter the first number: "))  # Accepting first number
b = int(input("Enter the second number: ")) # Accepting second number
print("Enter which operation would you like to perform?")   # Asking for operation
print("\'1\' for Addition")
print("\'2\' for Subtraction")
print("\'3\' for Multiplication")
print("\'4\' for Division")
print("\'5\' for Modulus")
operation = int(input("Enter the operation: "))
if operation == 1:
  print(a, "+", b, "=", a+b)    # Addition
elif operation == 2:
  print(a, "-", b, "=", a-b)    # Subtraction
elif operation == 3:
  print(a, "*", b, "=", a*b)    # Multiplication
elif operation == 4:
  if b == 0:
    print("Cannot divide by zero")  # If the denominator is zero
  else:
    print(a, "/", b, "=", a/b)  # If the denominator is non-zero
elif operation == 5:
  print(a, "%", b, "=", a%b)    # Modulus
else:
  print("Invalid input")    # Invalid operation enetered