#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By Sak

import hashlib
import configparser
import requests
import os

def get_api_key(key_name):
  # Create the ConfigParser and load the file
  config = configparser.ConfigParser()
  config.read("C:/Users/Rexh/Desktop/GRC/IT102 - Scripting for Cybersecurity/secrets.ini")
  # Get the API key and return
  api_key = config["APIKeys"][key_name]
  return api_key

def get_file_path(file_name):
  script_path = os.path.realpath(__file__)
  script_dir = os.path.dirname(script_path)
  file_path = os.path.join(script_dir, file_name)
  return file_path

# Function to get SHA-256 hash of file
def get_sha256_file_hash(file_path):
  try:
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
      for chunk in iter(lambda: f.read(4096), b""):
        sha256.update(chunk)
    return sha256.hexdigest()
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None
  except IOError:
    print(f"Error reading file: {file_path}")
    return None

def get_vt_file_report(apikey, file_hash):
  url = "https://www.virustotal.com/api/v3/files/" + file_hash
  headers = {
      "accept": "application/json",
      "x-apikey": apikey
  }
  response = requests.get(url, headers=headers)
  print(response.text)
  return response

# Get filename to scan
file_name = input("What file do you want to scan? ")
# Get file path
file_path = get_file_path(file_name)
# Get hash of file
file_hash = get_sha256_file_hash(file_path)
# Get api key
apikey = get_api_key("virustotal")
# Call file_report endpoint with hash
get_vt_file_report(apikey, file_hash)
# if results, print and quit
# Call file_upload endpoint with file
# Loop 5 times
  # Wait 20 seconds
  # Call file_report endpoint with hash
  # if results, print and quit
# Print, try again later