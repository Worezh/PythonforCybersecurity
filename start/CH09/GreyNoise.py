#!/usr/bin/env python3
# Script that scans IP using GreyNoise
# https://docs.greynoise.io
# By Sak


import requests
import configparser
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

def scan_ip(api_key, ip):
  url = "https://api.greynoise.io/v3/community/" + ip

  headers = {
      "accept": "application/json",
      "key": api_key
  }

  response = requests.get(url, headers=headers)
  return response

api_key = get_api_key("GreyNoise")
ip = input("What IP do you want to scan? ")
response = scan_ip(api_key, ip)
print(response.text)