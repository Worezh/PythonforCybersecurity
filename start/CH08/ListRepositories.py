#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By Sak

import requests
import configparser
def get_api_key(key_name):
  # Create the ConfigParser and load the file
  config = configparser.ConfigParser()
  config.read("C:/Users/Rexh/Desktop/GRC/IT102 - Scripting for Cybersecurity/secrets.ini")
  # Get the API key and return
  api_key = config["APIKeys"][key_name]
  return api_key

def list_repositories(token):
  url = "https://api.github.com/user/repos"

  payload = {}
  headers = {
    'Authorization': 'Bearer ' + token
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  return response.text

# Get API key
api_key = get_api_key("GitHub")

# Get repos and print
response = list_repositories(api_key)
print(response)
