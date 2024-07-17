"""WAP to ask a question to the user which will yield a numeric answer. Check if the user has given the right or wrong answer. Use IF ELSE condition."""

question = "What is the value of pi? (up to 2 decimal places)"
correctAnswer = 3.14
print(question)
userAnswer = float(input("Your answer: "))
if userAnswer == correctAnswer:
    print("Correct Answer!")
else:
    print("Wrong Answer")