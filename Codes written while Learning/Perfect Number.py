number = int(input("Enter a number: "))     # Asking user input
sum = 0
for i in range(1, number):      # Starting the loop
  if number%i==0:       # Checking for condition
    sum = sum + i       # Adding i to sum
  else:
    continue
if sum==number:     # Checking for condition
  print("It is a perfect number.")      # True Statement
else:
  print("It is not a perfect number.")      # False Statement