def fibonacci(n):       # Function to calculate fibonacci
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)      # Calculating fibonacci
for i in range(8):
  print(fibonacci(i), end = " ")        # Printing the series