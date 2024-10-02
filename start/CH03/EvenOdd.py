#!/usr/bin/env python3
# Checking if a number is even or odd
# By Sak 9/30

user_input = input("Enter a number: ")
num = int(user_input)

if num % 2 == 0:
  print(f"{num} is Even")
else:
  print(f"{num} is NOT Even")