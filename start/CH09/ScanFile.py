#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By Sak

import requests
import os
import configparser

class ScanFileResponse:
  def __init__(self, data):
    self.type = data['type']
    self.id = data['id']

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

# Upload file and get scan file ID
def get_scan_file_id(api_key, file_name):
  # Get file path
  file_path = get_file_path(file_name)

  url = "https://www.virustotal.com/api/v3/files"

  files = { "file": ("test.json", open(file_path, "rb")) }
  headers = {
    "accept": "application/json",
    "x-apikey": api_key
  }

  response = requests.post(url, files=files, headers=headers).json()
  result = ScanFileResponse(response["data"])
  return result.id

# Get analysis result from scan file ID
def get_analysis_result(api_key, analysis_id):
  url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

  headers = {
    "accept": "application/json",
    "x-apikey": api_key
  }

  response = requests.get(url, headers=headers).json()
  return response

def main():
  api_key = get_api_key("VirusTotal")
  analysis_id = get_scan_file_id(api_key, "test.json")
  result = get_analysis_result(api_key, analysis_id)
  print(result)

if __name__ == "__main__":
  main()