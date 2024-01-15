number = int(input("Enter a number: "))    # Asking user input
remainder = 0
sum = 0
power = 0
originalNumber = number
while number!=0:    # Loop to find the power
  remainder = number % 10
  power = power + 1
  number = number // 10
temp = originalNumber
while temp!=0:    # Loop to find the sum of the digits
  remainder = temp % 10
  sum = sum + pow(remainder, power)
  temp = temp // 10
if sum == originalNumber:   # True Condition
    print(originalNumber ,"is an Armstrong Number")
else:    # False Condition
    print(originalNumber ,"is not an Armstrong Number")