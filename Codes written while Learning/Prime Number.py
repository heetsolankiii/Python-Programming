number = int(input("Enter a number: "))    # Asking user input
count = 0
for i in range(1, number+1):    
  if number % i == 0:    # Checking for condition
    count = count + 1    # If true, count is incremented by 1
  else:
    continue
  i = i + 1
if count == 2:    # If count is 2, then it is prime
  print("The number is prime")
else:    # If count is not 2, then it is not prime
  print("The number is not prime")