#!/usr/bin/env python3
# Guess a number game
# Guess a number between 1 and 10
# Try to find the correct answer
# By Sak

import random

def generate_random_number():
  return random.randint(1, 10)

def ask_user_for_number():
  while True:
    try:
      return int(input("Guess a number: "))
    except ValueError:
      print("Please enter a valid integer number.")

def compare_numbers(rnd_num, guess_num):
  if rnd_num == guess_num:
    print(f"Congrats! You guessed the number! It was the number \"{rnd_num}\"!")
    exit()
  elif guess_num > rnd_num:
    print(f"{guess_num} is too high!\n")
  elif guess_num < rnd_num:
    print(f"{guess_num} is too low!\n")

def welcome():
  print("----------------------------------")
  print("Welcome to the Guess a Number game!")
  print("You have to guess a number between 1 and 10")
  print("Try to find the correct answer!")
  print("You have 5 tries.")
  print("Good luck!")
  print("----------------------------------")

def main():
  welcome()
  rnd_num = generate_random_number()
  for i in range(5):
    guess_num = ask_user_for_number()
    compare_numbers(rnd_num, guess_num)
    if i == 4:
      print(f"Game over! The correct answer was \"{rnd_num}\".")

if __name__ == "__main__":
  main()
  
