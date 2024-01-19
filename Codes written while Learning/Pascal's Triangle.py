# Initializing the variables
outerValue = 0
innerValue = 0
space = 5

for outerValue in range(5):    # Used to print outer values
  for space in reversed(range(5)):    # Used to print spaces
    if space > outerValue:
      print(" ", end="")
  num = 1
  for innerValue in range(5):    # Used to print inner values
    if innerValue <= outerValue:
      print(num, " ", end="")    # Used to print numbers
      num = (num * (outerValue - innerValue) // (innerValue + 1))    # Used to increment inner values
  print('\n')