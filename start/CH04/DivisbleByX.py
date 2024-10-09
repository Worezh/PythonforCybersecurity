#!/usr/bin/env python3
# Checking if a number is divisble by X
# By Sak

# function to ask for a number and divisor and return if number is divisble by divisor
def askUserInput():
  number = input("Enter a number: ")
  divisor = input("Enter the divisor: ")
  number = int(number)
  divisor = int(divisor)
  return number, divisor

def isDivisible(number, divisor):
  if number % divisor == 0:
    return True
  else:
    return False
  
number, divisor = askUserInput()
if isDivisible(number, divisor):
  print(f"{number} is divisible by {divisor}")
else:
  print(f"{number} is NOT divisible by {divisor}")
  
# def main():
#   number, divisor = askUserInput()
#   if isDivisible(number, divisor):
#     print(f"{number} is divisible by {divisor}")
#   else:
#     print(f"{number} is NOT divisible by {divisor}")
  
# if __name__ == "__main__":
#   main()