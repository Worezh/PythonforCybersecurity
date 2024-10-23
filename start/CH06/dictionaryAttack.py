#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 

import crypt
import os
import sys

# function to hash password
def hash_password(password, password_salt):
  pass_hash = crypt.crypt(password, password_salt)
  return pass_hash

# Ask user for hash_salt
password_salt = input("What is the hash salt? ")

# Ask user for the hash to compare
password_hash = input("What is the full hash? ")

# Get current file directory
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

# Open dictionary file
# Set the file path
file_path = os.path.join(script_dir, "top1000.txt")
with open(file_path, "r") as file:
  # Read each line in the file
  # passwords = file.read().splitlines()
  for guess in file:
    guess = guess.strip()
    # hash attempt using salt
    hashed_guess = hash_password(guess.strip(), password_salt)
    # Compare hashes
    if hashed_guess == password_hash:
      # Sucess - print and quit
      print(f"Password found: {guess}")
      sys.exit()
      
# print no password found
print("No password found")
