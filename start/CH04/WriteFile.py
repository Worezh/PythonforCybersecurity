#!/usr/bin/env python3
# Sample script that writes to a file
# By Sak

import os

# function to ask user information
def get_user_info():
  name = input("What is your name? ")
  favColor = input("What is your favorite color? ")
  petName = input("What is your pet's name? ")
  motherName = input("What is your mother's maiden name? ")
  elementarySchool = input("What elementary school did you attend? ")
  return name, favColor, petName, motherName, elementarySchool

# Get current file directory
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

# Set the file path
file_path = os.path.join(script_dir, "hackme.txt")

# Get user information
name, favColor, petName, motherName, elementarySchool = get_user_info()

# Write user information
with open(file_path, "w") as file:
  file.write(f"Name: {name}\n")
  file.write(f"Favorite Color: {favColor}\n")
  file.write(f"Pet Name: {petName}\n")
  file.write(f"Mother's Maiden Name: {motherName}\n")
  file.write(f"Elementary School: {elementarySchool}\n")

# Print user information
with open(file_path, "r") as file:
  print("\nHere is someone to hack - information")
  print("======================================")
  print(file.read())
  print("======================================")