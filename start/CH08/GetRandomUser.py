#!/usr/bin/env python3
# Script that get random user from https://randomuser.me/
# https://randomuser.me/api/
# By Sak

import requests
from datetime import datetime 
from UserResponse import UserResponse

def get_random_user():
  url = "https://randomuser.me/api/"
  response = requests.get(url)
  data = response.json()
  user_data = UserResponse(data['results'][0])
  return user_data

def get_gender(user_data):
  output = user_data.gender.capitalize()
  return output

def get_title(user_data):
  output = user_data.name.title
  return output

def get_full_name(user_data):
  output = f"{user_data.name.first} {user_data.name.last}"
  return output

def get_address(user_data):
  output = f"St. {user_data.location.street.number} {user_data.location.street.name}, {user_data.location.city}, {user_data.location.state} {user_data.location.country}, {user_data.location.postcode}"
  return output

def get_email(user_data):
  output = user_data.email
  return output

def get_dob(user_data):
  date_string = user_data.dob.date
  date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
  month_name = date_object.strftime("%B")
  output = f"{month_name} {date_object.day}, {date_object.year}"
  return output

def get_age(user_data):
  output = user_data.dob.age
  return output

def get_phone(user_data):
  output = user_data.phone
  return output

def get_cell(user_data):
  output = user_data.cell
  return output

user_data = get_random_user()
print("-----------------------------------")
print(f"Title/Prefix: {get_title(user_data)}.")
print(f"Full Name: {get_full_name(user_data)}")
print(f"Gender: {get_gender(user_data)}")
print("-----------------------------------")
print(f"Address: {get_address(user_data)}")
print(f"Email: {get_email(user_data)}")
print("-----------------------------------")
print(f"DOB: {get_dob(user_data)}")
print(f"Age: {get_age(user_data)}")
print("-----------------------------------")
print(f"Phone: {get_phone(user_data)}")
print(f"Cell: {get_cell(user_data)}")
print("-----------------------------------")