#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By 

import datetime
import os
import platform

# Function for pinging IP address
def ping_ip_address(ipAddress):
  # Get current OS
  currentOS = platform.system().lower()

  # Build ping command based on OS
  if currentOS == "windows":
    command = f"ping -n 1 -w 1000 {ipAddress} > NUL" # Windows
  else:
    command = f"ping -c 1 -w 1000 {ipAddress} > /dev/null 2>&1" # Linux

  # Run ping command and get exit code
  return os.system(command)

# Write log to file
def write_to_log(message):
  # script_dir = os.path.dirname(os.path.realpath(__file__))
  script_path = os.path.realpath(__file__)
  script_dir = os.path.dirname(script_path)
  file_path = os.path.join(script_dir, "pinger.log")
  
  # Get current date and time and Join date and message
  now = str(datetime.datetime.now()) + "\t"
  message = now + str(message) + "\n"

  # Open file in append mode and Write message to file
  with open(file_path, "a") as log_file:
    log_file.write(message)

for otect4 in range(10):
  ipAddress = f"192.168.0." + str(otect4 + 1)
  output = ""

  result = ping_ip_address(ipAddress)
  if result == 0:
    output = f"Ping to {ipAddress} - Success"
    print(output)
    write_to_log(output)
  else:
    output = f"Ping to {ipAddress} - Failure"
    print(output)
    write_to_log(output)