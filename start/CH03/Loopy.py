#!/usr/bin/env python3
# example workign with Loops
# By Sak

def askUserLoopWithReturn(userInput):
  output = ""
  if userInput == "y":
    for i in range(10):
      output += f"{i+1}: Yes, it is a good day!\n"
  elif userInput == "n":
    output += "No, today is not a good day...\n"
  else: 
    output += "Invalid Input. Please enter 'y' or 'n'.\n"
  return output

def send_message(userInput):
  if userInput == "y":
    for i in range(10):
      print(f"{i+1}: Yes, it is a good day!")
  elif userInput == "n":
    print("No, today is not a good day...")
  else:
    print("Invalid Input. Please enter 'y' or 'n'.")

userInput = input("Is today a good day? (y/n) ")
userInput = userInput.lower()
print()

send_message(userInput)
# print(askUserLoopWithReturn(userInput))