#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By Sak

import hashlib
import configparser
import time
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
  """
  Gets the SHA-256 hash of a given file.

  Args:
    file_path (str): The path to the file to get the hash for.

  Returns:
    str: The SHA-256 hash of the given file, or None if the file does not exist or
      cannot be read.
  """
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
  if response.status_code == 200:
    vt_report = response.json()
    return vt_report
  else:
    return None

def upload_vt_file(apikey, file_path):
  url = "https://www.virustotal.com/api/v3/files"
  files = { "file": ("test.json", open(file_path, "rb")) }
  headers = {
      "accept": "application/json",
      "x-apikey": apikey
  }
  response = requests.post(url, files=files, headers=headers)
  if response.status_code == 200:
    file = response.json()
    return file

# Get filename to scan
file_name = input("What file do you want to scan? ")

# Get file path
file_path = get_file_path(file_name)

# Get hash of file
file_hash = get_sha256_file_hash(file_path)

# Get api key
apikey = get_api_key("VirusTotal")

# Call file_report endpoint with hash
vt_file_report = get_vt_file_report(apikey, file_hash)

# if results, print and quit
if vt_file_report:
  # Capture the analysis stats
  vt_analysis_stats = vt_file_report['data']['attributes']['last_analysis_stats']
  # malicious, suspicious, undetected
  print(f"Malicious: {vt_analysis_stats['malicious']}")
  print(f"Suspicious: {vt_analysis_stats['suspicious']}")
  print(f"Undetected: {vt_analysis_stats['undetected']}")

# Call file_upload endpoint with file
upload_vt_file(apikey, file_path)

# Loop 5 times
for i in range(5):
  # Wait 20 seconds
  time.sleep(21)
  # Call file_report endpoint with hash
  vt_file_report = get_vt_file_report(apikey, file_hash)

  # if results, print and quit
  if vt_file_report:
    # Capture the analysis stats
    vt_analysis_stats = vt_file_report['data']['attributes']['last_analysis_stats']
    # malicious, suspicious, undetected
    print(f"Malicious: {vt_analysis_stats['malicious']}")
    print(f"Suspicious: {vt_analysis_stats['suspicious']}")
    print(f"Undetected: {vt_analysis_stats['undetected']}")

# Print, try again later
print("No results, please try again later!")