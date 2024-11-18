#!/usr/bin/env python3
# script that accesses Canvas API and list courses
# By Sak

import requests
import configparser

class CanvasCourses:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']

def get_api_key(key_name):
  # Create the ConfigParser and load the file
  config = configparser.ConfigParser()
  config.read("C:/Users/Rexh/Desktop/GRC/IT102 - Scripting for Cybersecurity/secrets.ini")
  # Get the API key and return
  api_key = config["APIKeys"][key_name]
  return api_key

def get_courses(token):
  url = "https://egator.greenriver.edu:443/api/v1/courses"
  headers = {
    'Authorization': 'Bearer ' + token,
  }

  response = requests.get(url, headers=headers)
  data = response.json()

  return [CanvasCourses(course) for course in data]

def main():
  api_key = get_api_key("Canvas")
  courses = get_courses(api_key)
  print("-----------------------------------")
  print("List of enrolled courses:")
  for course in courses:
    index = courses.index(course) + 1
    print(f"{index}. {course.name}")
  print("-----------------------------------")

if __name__ == "__main__":
  main()