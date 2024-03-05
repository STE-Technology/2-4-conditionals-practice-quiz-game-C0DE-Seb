"""
File: quiz.py
Author: Sebastian Sanchez
Date: 2024/03/04
Description: Multiple choice quiz with final score
"""

print("------------------------------- \
      \nMultiple-Choice Quiz Game")

#Initialize score
score = 0

#First question
print("\n1. What is the power house of the cell? \
      \n(a) Nucleus \
      \n(b) Mitochondria \
      \n(c) Cell Membrane \
      ")

answer = input("\n> ")

#Is the first users answer right
if answer == "b" or answer == "B":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#Second question
print("\n2. Who discovered gravity \
      \n(a) Isaac Newton \
      \n(b) Albert Einstein \
      \n(c) Charles Darwin \
      ")

answer = input("\n> ")

#Is the second users answer right
if answer == "a" or answer == "A":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#Third question
print("\n3. Which element is a non-metal \
      \n(a) Iron \
      \n(b) Sodium \
      \n(c) Oxygen \
      ")

answer = input("\n> ")

#Is the third users answer right
if answer == "c" or answer == "C":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#Calculate final score
final_score = score / 3 * 100

#Final results
print("\nQuiz complete! \
      \nYou answered " + str(score) + " out of 3 questions correctly. Your score is " + str(round(final_score, 1)) + "% \
      \n-------------------------------")