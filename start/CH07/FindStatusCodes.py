#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Sak

import os
import re

def get_file_path(file_name):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, file_name)
    return file_path

print("Enter to default for access.log")
file_name = input("Which file to analyze? ") or "access.log"

# Get current file directory
file_path = get_file_path(file_name)

# Check if file exists
if not os.path.exists(file_path):
  print(f"\"{file_path}\" does not exist in this directory.")
  exit()

# regex pattern
pattern = r"\s\d{3}\s"

# create empty dictionary
access_dict = {}

# Open file in read mode
with open(file_path, "r") as file:
  # Read file line by line
  for line in file:
    m = re.search(pattern, line)
    # check pattern match any line
    if m:
      client_status = m.group().strip()
      # increment count if status found
      if client_status in access_dict.keys():
        access_dict[client_status] += 1
      # create new key if not found
      else:
        access_dict[client_status] = 1

sorted_dict = dict(sorted(access_dict.items(), key=lambda item: item[1], reverse=True))
for key, value in sorted_dict.items():
  print(f"Status Code: {key}: {value} times")

# # sort dictionary by value
# for w in sorted(access_dict, key=access_dict.get, reverse=False):
#     print(w, access_dict[w])


