"""
File: quiz.py
Author: Sebastian Sanchez
Date: 2024/03/04
Description: Multiple choice quiz with final score
"""

print("-------------------------------")
print("Multiple-Choice Quiz Game")

#Initialize score
score = 0

#First question
print("\n1. What is the power house of the cell?")
print("(a) Nucleus")
print("(b) Mitochondria")
print("(c) Cell Membrane")

first_answer = input("\n> ")

#Is the first users answer right
if first_answer == "b":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#Second question
print("\n2. Who discovered gravity")
print("(a) Isaac Newton")
print("(b) Albert Einstein")
print("(c) Charles Darwin")

second_answer = input("\n> ")

#Is the second users answer right
if second_answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#Third question
print("\n3. Which element is a non-metal")
print("(a) Iron")
print("(b) Sodium")
print("(c) Oxygen")

third_answer = input("\n> ")

#Is the third users answer right
if third_answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#Calculate final score
final_score = score / 3 * 100

#Final results
print("\nQuiz complete!")
print("You answered " + str(score) + " out of 3 questions correctly. Your score is " + str(round(final_score, 1)) + "%")
print("-------------------------------")