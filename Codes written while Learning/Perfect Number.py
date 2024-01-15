number = int(input("Enter a number: "))
sum = 0
for i in range(1, number):
  if number%i==0:
    sum = sum + i
  else:
    continue
if sum==number:
  print("It is a perfect number.")
else:
  print("It is not a perfect number.")