import random as r

randomNumber = r.randint(1,20)
print("A random number between 1 to 20 is generated.")
chances = 3
print("You have 3 chances to guess the number.")
print("Let's start!")
while chances > 0:
  userInput = int(input("Enter your guess: "))
  if userInput == randomNumber:
    print("Congratulations! You guessed the number correctly.")
    break
  elif userInput > randomNumber:
    print("Your guess is too high.")
  else:
    print("Your guess is too low.")
  chances -= 1
  print(f"You have {chances} chances left.")
  if chances == 0:
    print("You have run out of chances. The number was", randomNumber)
    break

print("Thank you for playing!")