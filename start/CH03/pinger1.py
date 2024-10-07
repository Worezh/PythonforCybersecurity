#!/usr/bin/env python3
# First example of pinging from Python
# By Sak 9/30

# command = "ping -c 1 -w 2 127.0.0.1 > /dev/null 2>&1"
# Linux command

import os
import platform
currentOS = platform.system().lower()

ipAddress = "127.0.0.1"
if currentOS == "windows":
  command = f"ping -n 1 -w 1000 {ipAddress} > NUL" # Windows
else:
  command = f"ping -c 1 -w 1000 {ipAddress} > /dev/null 2>&1" # Linux

res = os.system(command)
if res == 0:
  print(f"Ping to {ipAddress} Success")
else:
  print(f"Ping to {ipAddress} Failure")