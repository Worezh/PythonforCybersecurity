#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Sak

# # Ask user for message
# initial_message = input("What is the message? ")
# final_message = ""

# # Convert message to lower case
# initial_message = initial_message.lower()

# # Loop each letter in message
# for letter in initial_message:
#   # Convert letter to number
#   ascii_num = ord(letter)

#   # Check if the character is a lower case letter
#   if ascii_num >= 97 and ascii_num <= 122:
#     # Add 13 to number
#     ascii_num = ascii_num + 13
    
#     # IS this past "z"
#     if ascii_num > 122:
#       # subtract 26
#       ascii_num = ascii_num - 26
  
#   # Convert back to letter
#   new_letter = chr(ascii_num)
#   final_message += new_letter

# # Print final message
# print(final_message)

# Encrypts/decrypts text using ROT13.
def rot13(text):
  output = ""
  for char in text:
    ascii_num = ord(char)
    if char.isalpha():
      ascii_num += 13
    output += chr(ascii_num) if ascii_num <= 122 else chr(ascii_num - 26)

  return output

initial_message = input("What is the message? ")
encrypted_message = rot13(initial_message)
print(encrypted_message, "\n")

# for letter in user_input:
#   if letter.isupper():
#     print(chr((ord(letter) - 65 + 13) % 26 + 65), end="")
#   elif letter.islower():
#     print(chr((ord(letter) - 97 + 13) % 26 + 97), end="")
#   else:
#     print(letter, end="")