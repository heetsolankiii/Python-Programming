def factorial(n):       # Function to calculate factorial
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
n = int(input("Enter a number: "))      # Accepting user input
print(f"{n}! = {factorial(n)}")      # Printing and calling factorial