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

def check_pwned_password(hash5):
  url = f"https://api.pwnedpasswords.com/range/{hash5}"
  payload = {}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  
  return response
  # print(response.text)

# Get SHA-1 hash of password
def get_hash_parts(password):
  pass_hash = sha1_hash(password)
  # Slice password hash at the 5th character
  hash_start = pass_hash[:5]
  hash_end = pass_hash[5:].upper()
  return hash_start, hash_end

user_pass = input("What password do you want to test? ")
hash_start, hash_end = get_hash_parts(user_pass)

# Call API with SHA-1 hash first 5 characters
response = check_pwned_password(hash_start)
for line in response.text.splitlines():
  if hash_end in line:
    print(f"Your password has been found {line.split(':')[1]} times.")
    break

# print(response.text)