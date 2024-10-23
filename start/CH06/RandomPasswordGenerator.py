#!/usr/bin/env python3
# By Sak

import random
import string

def generate_password(length, symbols, numbers, lower, upper, exclude_similar, exclude_ambiguous, start_with_letter):
  full_char = ""
  similar_chars = "oO0iIlL1|!"
  ambiguous_chars = "{}[]()/\'\"!,;:>."

  # Check if any character option is selected
  if symbols:
    full_char += string.punctuation
  if numbers:
    full_char += string.digits
  if lower:
    full_char += string.ascii_lowercase
  if upper:
    full_char += string.ascii_uppercase

  # Exclude similar characters
  if exclude_similar:
    full_char = "".join(set(full_char) - set(similar_chars))

  # Exclude ambiguous characters
  if exclude_ambiguous:
    full_char = "".join(set(full_char) - set(ambiguous_chars))
  
  # Check if password should start with a letter
  if start_with_letter:
    letters = string.ascii_letters
    # Exclude similar characters for starting with a letters if needed
    if exclude_similar:
      letters = "".join(set(letters) - set(similar_chars))
    # Generate first character letter of the password
    first_char = random.choice(letters)
    # Generate the rest of the password minus 1 character
    password = "".join(random.choices(full_char, k=length - 1))
    # Return the combine password
    return first_char + password
  else:
    return "".join(random.choices(full_char, k=length))

def bool_input(prompt):
    return input(prompt).strip().lower() == 'y'

def ask_user():
  length = int(input("Length of password: "))
  symbols = bool_input("Include symbols? (y/n): ")
  numbers = bool_input("Include numbers? (y/n): ")
  lower = bool_input("Include lower case letters? (y/n): ")
  upper = bool_input("Include upper case letters? (y/n): ")
  exclude_similar = bool_input("Exclude similar characters? (y/n): ")
  exclude_ambiguous = bool_input("Exclude ambiguous characters? (y/n): ")
  start_with_letter = bool_input("Start with a letter? (y/n): ")
  multi_password = int(input("Amount of passwords to generate: "))

  return length, symbols, numbers, lower, upper, exclude_similar, exclude_ambiguous, start_with_letter, multi_password

def welcome():
  print("Welcome to the Random Password Generator!")
  print("------------------------------------------")
  print("Please follow the instructions below:\n")
  print("1. Password length must be between 4 and 300")
  print("2. You must select at least one character option ")
  print("   - Symbols (!@#$%^&*()-_=+[]{}<>/?|\\)")
  print("   - Numbers (0-9)")
  print("   - Lower case letters (a-z)")
  print("   - Upper case letters (A-Z)")
  print("3. Choose to exclude similar characters (o, 0, i, I, l, L, 1, | etc.)")
  print("4. Choose to exclude ambigious characters ({, }, [ ], (, ), /, \, ', \" etc.)")
  print("5. Choose to start the first character with a letter")
  print("6. Choose to generate multiple passwords")
  print("------------------------------------------\n")

def goodbye():
  print("Goodbye! See you next time!")


while True:
  welcome()
  length, symbols, numbers, lower, upper, exclude_similar, exclude_ambiguous, start_with_letter, multi_password = ask_user()

  if length < 4 or length > 300:
    print("Password length must be between 4 and 300")
    continue
  
  if not (symbols or numbers or lower or upper):
    print("You must select at least one character option")
    continue
  
  for i in range(multi_password):
    pass_result = generate_password(length, symbols, numbers, lower, upper, exclude_similar, exclude_ambiguous, start_with_letter)
    colored_pass = ""
    for char in pass_result:
      if char.isalpha():
        colored_pass += "\033[91m" + char + "\033[0m"
      elif char.isdigit():
        colored_pass += "\033[94m" + char + "\033[0m"
      else:
        colored_pass += "\033[92m" + char + "\033[0m"
    print(f"{i+1}: {colored_pass}")

  cont = input("\nWould you like to generate more passwords? (y/n): ")
  if cont.lower() != 'y':
    goodbye()
    break

