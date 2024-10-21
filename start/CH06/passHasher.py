#!/usr/bin/env python3
# Script that hashes a password
#By 

# Sample data
# Password: Password01
# Salt: G.DTW7g9s5U7KYf5
# SHA-512 result: $6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.
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

# Usage example
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
shadowFile = os.path.join(script_dir, "shadow")
passwordFile = os.path.join(script_dir, "top1000.txt")

dictionary_passwords = read_dictionary_file(passwordFile)
shadow_entries = read_shadow_file(shadowFile)
crack_passwords(shadow_entries, dictionary_passwords)