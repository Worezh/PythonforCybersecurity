#!/usr/bin/env python3
# First example of pinging from Python
# By Sak 9/30

import os
import platform
# Get current OS
currentOS = platform.system().lower()

for otect4 in range(10):
  ipAddress = f"192.168.0." + str(otect4 + 1)

  # Build ping command based on OS
  if currentOS == "windows":
    command = f"ping -n 1 -w 1000 {ipAddress} > NUL" # Windows
  else:
    command = f"ping -c 1 -w 1000 {ipAddress} > /dev/null 2>&1" # Linux

  # Run ping command and get exit code
  res = os.system(command)
  if res == 0:
    print(f"Ping to {ipAddress} Success")
  else:
    print(f"Ping to {ipAddress} Failure")