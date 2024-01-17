questions = [
  [ # Question 1
    "What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1
  ],
  [ # Question 2
    "In which year did India gain independence from British rule?", "1940", "1948", "1947", "1950", 3
  ],
  [ # Question 3
    "Which of these monuments is NOT located in Delhi?", "Qutub Minar", "Taj Mahal", "Red Fort", "India Gate", 2
  ],
  [ # Question 4
    "Which Indian state is known as the \"Land of Spices\"?", "Kerala", "Karnataka", "Maharashtra", "Tamil Nadu", 1
  ],
  [ # Question 5
    "Which city is known as the \"Silicon Valley of India\"?", "Mumbai", "Bangalore", "Chennai", "Kolkata", 2
  ],
  [ # Question 6
    "Which mountain range separates India from China?","Himalayas", "Karakoram", "Hindu Kush", "Andes", 1
  ],
  [ # Question 7
    "Which Indian city is famous for its Bollywood film industry?", "Mumbai", "Delhi", "Kolkata", "Chennai", 1
  ],
  [ # Question 8
    "Which ancient Indian civilization is known for its Mohenjo-daro and Harappa ruins?", "Vedic Civilization", "Mauryan Empire", "Gupta Empire", "Indus Valley Civilization", 4
  ],
  [ # Question 9
    "Which Indian city is known as the \"City of Dreams\"?", "Mumbai", "Delhi", "Kolkata", "Chennai", 1
    
  ],
  [ # Question 10
    "Which Indian state is known as the \"Land of Elephants\"?", "Kerala", "Karnataka", "Maharashtra", "Tamil Nadu", 1
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(0, len(questions)):
  question = questions[i]
  print(f"Question for Rs. {levels[i]}\n")
  print(f"{question[0]}")
  print(f"a. {question[1]}      b. {question[2]} ")
  print(f"c. {question[3]}      d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or 0 to quit: "))
  if reply == 0:
    money = 0
    break
  if reply == question[-1]:
    print(f"\nCorrect answer, you have won Rs. {levels[i]}\n")
    if i == 2:
      money = 3000
    elif i == 5:
      money = 10000
    elif i == 8:
      money = 160000
    elif i == 9:
      money = 320000
      break
  else:
    print("\nWrong answer!")
    break
if money == 0:
  print("\nUnfortunately, you have not won any money.")
else:
  print(f"\nCONGRATULATIONS")
  print(f"You have won Rs. {money}")
print("Thank you for playing Kaun Banega Crorepati!")