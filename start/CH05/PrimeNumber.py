#!/usr/bin/env python3
# Prime Number Checker
# By Sak

import math

# Function to check if a number is prime
def isPrimeNumber(number):
  if number <= 1:
    return False
  
  # Only checks up to the square root of the number to avoid iterating too many times for large numbers
  for i in range(2, int(math.sqrt(number) + 1)):
    if number % i == 0:
      return False
  return True

number = int(input("Enter a positive integer number: "))
if isPrimeNumber(number):
  print(f"{number} is a prime number\n")
else:
  print(f"{number} is NOT a prime number\n")