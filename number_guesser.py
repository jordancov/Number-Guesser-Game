#importing packages
import random
from tokenize import cookie_re

#Defining random numbers
number_one_range = 0
number_two_range = 20
correctAnswer = random.randrange(number_one_range, number_two_range)
print(correctAnswer)

#Intial input from user
print("Hello! Please enter your name")
name = input("Enter name: ")
print("Welcome", name, "this is the number guesser game")
print("Please guess a number between", number_one_range, "and", number_two_range)
userAnswer = int(input("Enter number: "))

attempts = 0

#While statement to capture the answer from the user and check if correct or not
while(True):
    if userAnswer != correctAnswer:
        print("WRONG ANSWER TRY AGAIN") 
        attempts += 1
        userAnswer = int(input("Enter number: "))
    if userAnswer == correctAnswer:
        if attempts == 0:
            print("WOW AMAZING!!! You got this correct first time. Kudos :D")
            break
        elif attempts == 1:
            print("Correct! It took you", attempts, "attempt to get this correct. Keep going until you get it first time!")
            break
        else:
            print("Correct! It took you", attempts, "attempts to get this correct. Keep going until you get it first time!")
            break
        
