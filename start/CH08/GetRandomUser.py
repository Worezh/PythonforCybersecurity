#!/usr/bin/env python3
# Script that get random user from https://randomuser.me/
# https://randomuser.me/api/
# By Sak

import requests
from datetime import datetime 
from UserResponse import UserResponse

def get_random_user(user_count):
  url = f"https://randomuser.me/api/?results={user_count}"
  response = requests.get(url)
  data = response.json()
  users = []
  for user in data['results']:
    users.append(UserResponse(user))
  # users = UserResponse(data['results'])
  return users

def get_gender(user):
  output = user.gender.capitalize()
  return output

def get_name_title(user):
  name = user.name
  full_name = f"{name.first} {name.last}"
  title = name.title
  return full_name, title

def get_address(user):
  location = user.location
  street = location.street
  output = f"St. {street.number} {street.name}, {location.city}, {location.state} {location.country}, {location.postcode}"
  return output

def get_credentials(user):
  username = user.login.username
  password = user.login.password
  return username, password

def get_email(user):
  output = user.email
  return output

def get_dob_age(users):
  date_string = users.dob.date
  date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
  month_name = date_object.strftime("%B")
  dob = f"{month_name} {date_object.day}, {date_object.year}"
  age = user.dob.age
  return dob, age

def get_cell_phone(users):
  phone = users.phone
  cell = users.cell
  return phone, cell

users = get_random_user(5)
for user in users:
  full_name, title = get_name_title(user)
  gender = get_gender(user)
  address = get_address(user)
  email = get_email(user)
  dob, age = get_dob_age(user)
  username, password = get_credentials(user)
  phone, cell = get_cell_phone(user)

  print(f"\n\033[92mUser {users.index(user) + 1}\033[0m")
  print("-----------------------------------")
  print(f"Title/Prefix: {title}.")
  print(f"Full Name: {full_name}")
  print(f"Gender: {gender}")
  print("-----------------------------------")
  print(f"Address: {address}")
  print(f"Email: {email}")
  print("-----------------------------------")
  print(f"Username: {username}")
  print(f"Password: {password}")
  print("-----------------------------------")
  print(f"DOB: {dob}")
  print(f"Age: {age}")
  print("-----------------------------------")
  print(f"Phone: {phone}")
  print(f"Cell: {cell}")
  print("-----------------------------------")