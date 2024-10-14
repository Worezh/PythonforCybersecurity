#!/usr/bin/env python3
# example workign with conditionals
# By Sak

def askUserWithReturn(userInput):
  output = None
  if userInput == "y":
    output = "Yeah, it is a good day!"
  elif userInput == "n":
    output = "No, today is not a good day..."
  else:
    output = "Invalid Input. Please enter 'y' or 'n'."
  return output

def send_message(userInput):
  if userInput == "y":
    print("Yeah, it is a good day!")
  elif userInput == "n":
    print("No, today is not a good day...")
  else:
    print("Invalid Input. Please enter 'y' or 'n'.")

userInput = input("Is today a good day? (y/n) ")
userInput = userInput.lower()
print()

send_message(userInput)
# print(askUserWithReturn(userInput))