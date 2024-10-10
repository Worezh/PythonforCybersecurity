#!/usr/bin/env python3
# Checking if a number is divisble by X
# By Sak

# User Input Function
def askUserInput():
  number = input("Enter a number: ")
  divisor = input("Enter the divisor: ")
  number = int(number)
  divisor = int(divisor)
  return number, divisor

# Divisibility Function
def isDivisible(number, divisor):
  if number % divisor == 0:
    return True
  else:
    return False
  
number, divisor = askUserInput()
if isDivisible(number, divisor):
  print(f"\n== {number} is divisible by {divisor} ==\n")
else:
  print(f"\n== {number} is NOT divisible by {divisor} ==\n")
  
# def main():
#   number, divisor = askUserInput()
#   if isDivisible(number, divisor):
#     print(f"{number} is divisible by {divisor}")
#   else:
#     print(f"{number} is NOT divisible by {divisor}")
  
# if __name__ == "__main__":
#   main()