#!/usr/bin/env python3
# First example of pinging from Python
# By Sak 9/30

import os

#command = "ping -c 1 -w 2 127.0.0.1 > /dev/null 2>&1"
# This command will not work on Windows
command = "ping -n 1 -w 2 8.8.8.8 > NUL 2>&1"

res = os.system(command)
print("Result:", res)