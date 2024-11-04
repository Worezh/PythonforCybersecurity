#!/usr/bin/env python3
# Script that scans web server logs for client addresses
# Use RegEx to find and report on most accessed resources
# By Sak

import os
import re

# \033[91m to makes the text red
# \033[0m to resets the color after the text
def red_text(text):
  return "\033[91m" + text + "\033[0m"

# \033[92m to makes the text green
def green_text(text):
  return "\033[92m" + text + "\033[0m"

# Get file path function
def get_file_path(file_name):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, file_name)
    return file_path

# Check if file exists function
def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"\"{file_path}\" does not exist in this directory.")
        exit()

print("Enter to default for access.log")
file_name = input("Which file to analyze? ") or "access.log"

# Get current file directory and check if file exists
file_path = get_file_path(file_name)
check_file_exists(file_path)

# regex pattern
pattern = r"(?:GET|POST) ([^ ]+)"

# create empty dictionary
access_dict = {}

# Open file in read mode
with open(file_path, "r") as file:
  # Read file line by line
  for line in file:
    m = re.search(pattern, line)
    # check pattern match any line
    if m:
      client_status = m.group(1).strip()
      # increment count if status found
      if client_status in access_dict.keys():
        access_dict[client_status] += 1
      # create new key if not found
      else:
        access_dict[client_status] = 1

# Sort the dictionary by value in descending order
sorted_dict = dict(sorted(access_dict.items(), key=lambda item: item[1], reverse=True))

# Print the top 10 most accessed resources
print("\nTop 10 Most Popular Resources:")
for key, value in list(sorted_dict.items())[:10]:
  print(f"Resource: {green_text(key)} - Requested {red_text(str(value))} times")

# Ask the user if they want the remaining resources to be printed out
response = input("\nDo you want to print the remaining resources? (y/n): ")
if response.lower() == "y":
  for key, value in list(sorted_dict.items())[10:]:
    print(f"Resource: {green_text(key)} - Requested {red_text(str(value))} times")

# Write the output to a file
with open(get_file_path("popular_resources.txt"), "w") as file:
  file.write("Top 10 Most Popular Resources:\n")
  for key, value in list(sorted_dict.items())[:10]:
    file.write(f"Resource: {key} - Requested {value} times\n")
  file.write("Remaining Resources:\n")
  for key, value in list(sorted_dict.items())[10:]:
    file.write(f"Resource: {key} - Requested {value} times\n")

print("Output written to popular_resources.txt")