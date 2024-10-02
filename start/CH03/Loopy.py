#!/usr/bin/env python3
# example workign with Loops
# By Sak 10/02

user_input = input("Is today a good day? (y/n) ")
user_input = user_input.lower()

if user_input == "y":
  for i in range(10):
    print("Yes, it is a good day!")
elif user_input == "n":
  print("No, sadly, today is not a good day...")
else:
  print("I don't understand your input. Please enter 'y' or 'n'.")