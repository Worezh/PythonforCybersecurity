#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Sak

import os

def get_file_path(file_name):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, file_name)
    return file_path

print("Enter to default for access.log")
file_name = input("Which file to analyze? ") or "access.log"

# Get current file directory
file_path = get_file_path(file_name)
count = 0

# Check if file exists
if not os.path.exists(file_path):
  print(f"\"{file_path}\" does not exist in this directory.")
  exit()

# Open file in read mode
with open(file_path, "r") as file:
  # Read file line by line
  for line in file:
    # Check for 404 errors in lines
    if "404" in line:
      if "qwerty" in line:
        print(line.strip())
        # count += 1
    if "qwerty" in line:
      print(line.strip())
    # if count == 10:
    #   break

print(f"Number of 404 errors: {count}")
