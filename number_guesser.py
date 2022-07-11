#importing packages
import random

#Defining random numbers
numberOneRange = 0
numberTwoRange = 20
correctAnswer = random.randrange(numberOneRange, numberTwoRange)
print(correctAnswer)

#Intial input from user
print("Hello! Please enter your name")
name = input("Enter name: ")
print("Welcome", name, "this is the number guesser game")
print("Please guess a number between", numberOneRange, "and", numberTwoRange)
userAnswer = input("Enter number: ")

#While statement to capture the answer from the user
while(True):
    if userAnswer != correctAnswer:
        print("WRONG ANSWER TRY AGAIN") 
        userAnswer = int(input("Enter number: "))
    if userAnswer == correctAnswer:
        print("WOW well done you got the right number!")
        break
    
