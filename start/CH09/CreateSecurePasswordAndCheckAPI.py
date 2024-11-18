#!/usr/bin/env python3
# script that generates a random password and checks it against haveibeenpwned.com
# By Sak

import random
import string
import requests
import hashlib

def generate_password(length, symbols, numbers, lower, upper, exclude_similar, exclude_ambiguous, start_with_letter):
  full_char = ""
  similar_chars = "oO0iIlL1|!"
  ambiguous_chars = "{}[]()/\'\"!,;:>."

  # Add selected option to full character set for generating password
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
    # Generate the rest of the password minus 1 character for combining
    password = "".join(random.choices(full_char, k=length - 1))
    # Return the combine password
    return first_char + password
  else:
    return "".join(random.choices(full_char, k=length))
  
# Get SHA-1 hash of password
def sha1_hash(password):
  sha1 = hashlib.sha1()
  sha1.update(password.encode('utf-8'))
  return sha1.hexdigest()

# Get first 5 characters and remaining characters of SHA-1 hash
def get_hash_parts(password):
  pass_hash = sha1_hash(password).upper()
  # Slice password hash at the 5th character
  hash_start = pass_hash[:5]
  hash_end = pass_hash[5:]
  return hash_start, hash_end

def check_pwned_password(first_five):
  url = f"https://api.pwnedpasswords.com/range/{first_five}"
  response = requests.get(url)
  
  # Split the response into a list of lines
  pass_list = response.text.splitlines()
  # Split result on : and make it into a dictionary
  pass_dict = {}
  for pass_item in pass_list:
    pass_piece = pass_item.split(":")
    # Add password and count to dictionary
    pass_dict[pass_piece[0]] = pass_piece[1]

  return pass_dict

# Get user input
def bool_input(prompt):
    return input(prompt).strip().lower() == 'y'

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
  print("4. Choose to exclude ambigious characters ({, }, [ ], (, ), /, \\, ', \" etc.)")
  print("5. Choose to start the first character with a letter")
  print("6. Choose to generate multiple passwords")
  print("------------------------------------------")

def goodbye():
  print("Goodbye! See you next time!")

def red_text(text):
  return "\033[91m" + text + "\033[0m"

def main():
  welcome()
  while True:
    pass_list = []
    # Validate the length is between 4 and 300
    length = int(input("1. Length of password: "))
    if length < 4 or length > 300:
      print(red_text("\nPassword length must be between 4 and 300. Please try again.\n"))
      continue

    # check if any character option is selected
    symbols = bool_input("2. Include symbols? (y/n): ")
    numbers = bool_input("2. Include numbers? (y/n): ")
    lower = bool_input("2. Include lower case letters? (y/n): ")
    upper = bool_input("2. Include upper case letters? (y/n): ")
    if not (symbols or numbers or lower or upper):
      print(red_text("\nYou must select at least one character option. Please try again.\n"))
      continue

    # Ask for the rest of the options
    exclude_similar = bool_input("3. Exclude similar characters? (y/n): ")
    exclude_ambiguous = bool_input("4. Exclude ambiguous characters? (y/n): ")
    start_with_letter = bool_input("5. Start with a letter? (y/n): ")
    multi_password = int(input("6. Amount of passwords to generate: "))
    print("------------------------------------------")
    
    for _ in range(multi_password):
      pass_result = generate_password(length, symbols, numbers, lower, upper, exclude_similar, exclude_ambiguous, start_with_letter)
      pass_list.append(pass_result)

    for password in pass_list:
      hash_start, hash_end = get_hash_parts(password)
      response = check_pwned_password(hash_start)
      if hash_end in response:
        print(f"\"{password}\" was found {response[hash_end]} times")
      else:
        print(f"\"{password}\" is a secure password!")
    print("------------------------------------------")

    cont = input("\nWould you like to generate more passwords? (y/n): ")
    if cont.lower() != 'y':
      break
  goodbye()

if __name__ == "__main__":
  main()
