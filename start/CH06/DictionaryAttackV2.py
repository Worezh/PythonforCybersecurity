#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Sak

import crypt
import os

def read_dictionary_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

def read_shadow_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    shadow_entries = {}
    for line in lines:
        user, hashed_password = line.split(':')[:2]
        shadow_entries[user] = hashed_password
    return shadow_entries

def crack_passwords(shadow_entries, dictionary_passwords):
    for user, hashed_password in shadow_entries.items():
        for password in dictionary_passwords:
            if crypt.crypt(password, hashed_password) == hashed_password:
                print(f"Match found: User - {user}, Password - {password}")
                break
        print(f"No match found: User - {user}")

# Get current file directory
def get_file_path(file_name):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, file_name)
    return file_path

# Main
shadowFile = get_file_path("shadow")
passwordFile = get_file_path("top1000.txt")
dictionary_passwords = read_dictionary_file(passwordFile)
shadow_entries = read_shadow_file(shadowFile)
crack_passwords(shadow_entries, dictionary_passwords)