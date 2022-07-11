#importing packages
import random

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
userAnswer = input("Enter number: ")

#While statement to capture the answer from the user and check if correct or not
while(True):
    if userAnswer != correctAnswer:
        print("WRONG ANSWER TRY AGAIN") 
        userAnswer = int(input("Enter number: "))
    if userAnswer == correctAnswer:
        print("WOW well done you got the right number!")
        break
    
