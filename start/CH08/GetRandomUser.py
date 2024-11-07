#!/usr/bin/env python3
# Script that get random user from https://randomuser.me/
# https://randomuser.me/api/
# By Sak

import requests
from datetime import datetime
from UserResponse import UserResponse

class UserInfo:
  def __init__(self, user_info):
    self.title = user_info["title"]
    self.full_name = user_info["full_name"]
    self.gender = user_info["gender"]
    self.address = user_info["address"]
    self.email = user_info["email"]
    self.dob = user_info["dob"]
    self.age = user_info["age"]
    self.username = user_info["username"]
    self.password = user_info["password"]
    self.phone = user_info["phone"]
    self.cell = user_info["cell"]

def get_random_user(user_count):
  url = f"https://randomuser.me/api/?results={user_count}"
  response = requests.get(url)
  data = response.json()
  return [UserResponse(user) for user in data["results"]]

  # The above logic is a simplified version of the following:
  # users = []
  # for user in data['results']:
  #   users.append(UserResponse(user))
  # users = UserResponse(data['results'])
  # return users

def get_user_info(user):
  if user is None:
    return None
  user_info = {
    "title": user.name.title,
    "full_name": f"{user.name.first} {user.name.last}",
    "gender": user.gender.capitalize(),
    "address": f"St. {user.location.street.number} {user.location.street.name}, {user.location.city}, {user.location.state} {user.location.country}, {user.location.postcode}",
    "email": user.email,
    "dob": datetime.strptime(user.dob.date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%B %d, %Y"),
    "age": user.dob.age,
    "username": user.login.username,
    "password": user.login.password,
    "phone": user.phone,
    "cell": user.cell
  }
  return UserInfo(user_info)

def print_users(users):
  for user in users:
    index = users.index(user)
    user_info = get_user_info(user)
    if user_info is not None:
      print(f"\n\033[92mUser {index + 1}\033[0m")
      print("-----------------------------------")
      print(f"Title/Prefix: {user_info.title}.")
      print(f"Full Name: {user_info.full_name}")
      print(f"Gender: {user_info.gender}")
      print("-----------------------------------")
      print(f"Address: {user_info.address}")
      print(f"Email: {user_info.email}")
      print("-----------------------------------")
      print(f"Username: {user_info.username}")
      print(f"Password: {user_info.password}")
      print("-----------------------------------")
      print(f"DOB: {user_info.dob}")
      print(f"Age: {user_info.age}")
      print("-----------------------------------")
      print(f"Phone: {user_info.phone}")
      print(f"Cell: {user_info.cell}")
      print("-----------------------------------")
    else:
      print("No user information available")

def main():
  users = get_random_user(2)
  print_users(users)

if __name__ == "__main__":
  main()

# The original code before refactoring
# import requests
# from datetime import datetime 
# from UserResponse import UserResponse

# def get_random_user(user_count):
#   url = f"https://randomuser.me/api/?results={user_count}"
#   response = requests.get(url)
#   data = response.json()
#   users = []
#   for user in data['results']:
#     users.append(UserResponse(user))
#   # users = UserResponse(data['results'])
#   return users

# def get_gender(user):
#   output = user.gender.capitalize()
#   return output

# def get_name_title(user):
#   name = user.name
#   full_name = f"{name.first} {name.last}"
#   title = name.title
#   return full_name, title

# def get_address(user):
#   location = user.location
#   street = location.street
#   output = f"St. {street.number} {street.name}, {location.city}, {location.state} {location.country}, {location.postcode}"
#   return output

# def get_credentials(user):
#   username = user.login.username
#   password = user.login.password
#   return username, password

# def get_email(user):
#   output = user.email
#   return output

# def get_dob_age(user):
#   date_string = user.dob.date
#   date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
#   month_name = date_object.strftime("%B")
#   dob = f"{month_name} {date_object.day}, {date_object.year}"
#   age = user.dob.age
#   return dob, age

# def get_cell_phone(user):
#   phone = user.phone
#   cell = user.cell
#   return phone, cell

# def print_users(users):
#   for user in users:
#     index = users.index(user)
#     full_name, title = get_name_title(user)
#     gender = get_gender(user)
#     address = get_address(user)
#     email = get_email(user)
#     dob, age = get_dob_age(user)
#     username, password = get_credentials(user)
#     phone, cell = get_cell_phone(user)

#     print(f"\n\033[92mUser {index + 1}\033[0m")
#     print("-----------------------------------")
#     print(f"Title/Prefix: {title}.")
#     print(f"Full Name: {full_name}")
#     print(f"Gender: {gender}")
#     print("-----------------------------------")
#     print(f"Address: {address}")
#     print(f"Email: {email}")
#     print("-----------------------------------")
#     print(f"Username: {username}")
#     print(f"Password: {password}")
#     print("-----------------------------------")
#     print(f"DOB: {dob}")
#     print(f"Age: {age}")
#     print("-----------------------------------")
#     print(f"Phone: {phone}")
#     print(f"Cell: {cell}")
#     print("-----------------------------------")

# def main():
#   users = get_random_user(5)
#   print_users(users)

# if __name__ == "__main__":
#   main()