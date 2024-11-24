#!/usr/bin/env python3
# Script that scans files hashes using VirusTotal
# https://developers.virustotal.com/reference
# By Sak

import requests
import os
import hashlib
import configparser

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
    # return None
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
  
# Function to scan file
def scan_file_by_hash(key_name, file_name):
  # Get API key
  apikey = get_api_key(key_name)
  # Get file path
  file_path = get_file_path(file_name)
  # Get SHA-256 hash of file
  sha256_hash = get_sha256_file_hash(file_path)

  if sha256_hash:
    url = "https://www.virustotal.com/api/v3/files/" + sha256_hash
    headers = {
        "accept": "application/json",
        "x-apikey": apikey
    }
    response = requests.get(url, headers=headers)
    return response
  else:
    exit()

def main():
  response = scan_file_by_hash("VirusTotal", "test.json")
  print(response.text)

if __name__ == "__main__":
  main()