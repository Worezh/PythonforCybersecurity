#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created By Sak

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

userName = input("What is your name? ")
print(f"Hello {userName}!")
print("Hello " + userName + "!")
print("Hello {0}!".format(userName))
print("Hello", userName, "\b!\n")
print("Today is going to be a great day!\n")

userAge = int(input("What is your age? "))
print(f"In 2 years, you will be {userAge + 2} years old!\n")
