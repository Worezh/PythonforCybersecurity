#!/usr/bin/env python3
# Script that scans IP using Shodan
# https://developer.shodan.io
# By Sak

from shodan import Shodan
import configparser

def get_api_key(key_name):
  # Create the ConfigParser and load the file
  config = configparser.ConfigParser()
  config.read("C:/Users/Rexh/Desktop/GRC/IT102 - Scripting for Cybersecurity/secrets.ini")
  # Get the API key and return
  api_key = config["APIKeys"][key_name]
  return api_key

api_key = get_api_key("Shodan")

api = Shodan(f'{api_key}')
print(api.host('72.163.4.185'))