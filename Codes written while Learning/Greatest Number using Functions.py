def isGreater(a, b, c):  # Function to check which number is greater
  if (a>b):
    if (a>c):
      print(a, "is greater")
    else:
      print(c, "is greater")
  else:
    if (b>c):
      print(b, "is greater")
    else:
      print(c, "is greater")
    

a = int(input("Enter the first number: "))  # First Input
b = int(input("Enter the second number: "))  # Second Input
c = int(input("Enter the third number: "))  # Third Input
isGreater(a, b, c)