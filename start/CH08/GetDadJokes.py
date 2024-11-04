#!/usr/bin/env python3
# Script that get dad jokes from icanhazdadjoke.com
# https://icanhazdadjoke.com
# By Sak

import requests

class DadJokeResponse:
  def __init__(self, data):
    self.id = data['id']
    self.joke = data['joke']

def print_dad_joke(dad_joke_response):
  print(dad_joke_response.joke)

def get_dad_joke():
  url = "https://icanhazdadjoke.com/"
  headers = {"Accept": "application/json"}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    data = response.json()
    dad_joke_response = DadJokeResponse(data)
    return dad_joke_response
  else:
    return None

dad_joke_response = get_dad_joke()
print_dad_joke(dad_joke_response)

# if dad_joke_response:
#   print(dad_joke_response.id)
#   print(dad_joke_response.joke)
# else:
#   print("Failed to retrieve dad joke")