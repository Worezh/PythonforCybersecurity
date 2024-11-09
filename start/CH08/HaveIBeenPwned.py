#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Sak

import requests
import hashlib

def sha1_hash(password):
  sha1 = hashlib.sha1()
  sha1.update(password.encode('utf-8'))
  return sha1.hexdigest()

def check_pwned_password(first_five):
  url = f"https://api.pwnedpasswords.com/range/{first_five}"
  payload = {}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  
  # Split the response into a list of lines
  pass_list = response.text.splitlines()
  # Split result on : and make it into a dictionary
  pass_dict = {}
  for pass_item in pass_list:
    pass_piece = pass_item.split(":")
    # Add password and count to dictionary
    pass_dict[pass_piece[0]] = pass_piece[1]

  return pass_dict

# Get SHA-1 hash of password
def get_hash_parts(password):
  pass_hash = sha1_hash(password).upper()
  # Slice password hash at the 5th character
  hash_start = pass_hash[:5]
  hash_end = pass_hash[5:]
  return hash_start, hash_end

user_pass = input("What password do you want to test? ")
hash_start, hash_end = get_hash_parts(user_pass)

# Call API with SHA-1 hash first 5 characters
response = check_pwned_password(hash_start)

# Check if hash is in the dictionary
if hash_end in response:
  print(f"{user_pass} was found {response[hash_end]} times")
else:
  print(f"{user_pass} was not found")