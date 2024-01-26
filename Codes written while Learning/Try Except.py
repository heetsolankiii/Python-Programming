def tryExcept():
  try:
    number = int(input("Enter a number: "))    # Accepting Input
    print(number, "is an integer.")    # Printing Input
  except:
    print("It is not an integer")    # If not an Integer
    tryExcept()        # Calling the same function again

tryExcept()    # Calling the function