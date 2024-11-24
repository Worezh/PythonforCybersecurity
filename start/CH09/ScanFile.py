#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By Sak

import requests
import os
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

def scan_file(key_name, file_name):
  # Get API key
  api_key = get_api_key(key_name)
  # Get file path
  file_path = get_file_path(file_name)

  url = "https://www.virustotal.com/api/v3/files"

  files = { "file": ("test.json", open(file_path, "rb")) }
  headers = {
    "accept": "application/json",
    "x-apikey": api_key
  }

  response = requests.post(url, files=files, headers=headers)
  return response

def main():
  result = scan_file("VirusTotal", "test.json")
  print(result)

if __name__ == "__main__":
  main()