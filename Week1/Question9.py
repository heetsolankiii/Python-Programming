"""WAP to determine whether a number is divisible by 3, 5 or 9. Print the list of divisors (i.e. 3, 5 or 9) which are dividing the number."""

divisors = []
num = int(input("Enter a number: "))
if num % 3 == 0:
    divisors.append(3)
if num % 5 == 0:
    divisors.append(5)
if num % 9 == 0:
    divisors.append(9)


if divisors:
    print(num, "is divisible by", divisors)
else:
    print(num, "is not divisible by 3, 5 or 9")