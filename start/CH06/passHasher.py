#!/usr/bin/env python3
# Script that hashes a password
#By 

# Sample data
# Password: Password01
# Salt: G.DTW7g9s5U7KYf5
# SHA-512 result: $6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p.
import crypt

def testPass(hashedPass, salt, plaintextPass):
    # Hash the plaintext password with the salt
    hashedPlaintext = crypt.crypt(plaintextPass, salt)

    # Compare the hashes
    return hashedPlaintext == hashedPass

def main():
    # Prompt for hashed password from /etc/shadow
    hashedPass = "$6$G.DTW7g9s5U7KYf5$xTXAbS1Q30hfd10VDbkSh5adZMxbqRUMOyNyKopfFpMvD.Vf/CcoEBn/TUYcfJ1jAaEiJPBf/PoCLFq7U7Q7p."

    # Prompt for the SALT to use
    salt = input("Enter the SALT to use (e.g., $6$ruzSF91zH9x9MeX6): ")

    # Prompt for the file containing plaintext passwords
    passwordFile = "start/ch06/top1000.txt"

    # Open the password file
    try:
        with open(passwordFile, "r") as file:
            # Read each password from the file
            for line in file:
                # Strip the newline character
                plaintextPass = line.strip()

                # Try the password
                if testPass(hashedPass, salt, plaintextPass):
                    # If the password matches, print the result and quit
                    print(f"Password found: {plaintextPass}")
                    return
    except FileNotFoundError:
        print(f"File not found: {passwordFile}")

    # If no match is found, print a message
    print("No match found.")

if __name__ == "__main__":
    main()