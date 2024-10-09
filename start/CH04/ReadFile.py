#!/usr/bin/env python3
# Sample script that reads from a file
# By Sak
import os

# Get current file directory
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

# Set the file path
file_path = os.path.join(script_dir, "hackme.txt")

with open(file_path, "r") as file:
  print("Here is someone to hack - information")
  print("======================================")
  print(file.read())
  print("======================================")

# ipFiles = open("start/ch04/ips.txt", "r")

# # Read the contents of the file and print to screen
# ips = ipFiles.readlines()
# for ip in ips:
#   print(ip)

