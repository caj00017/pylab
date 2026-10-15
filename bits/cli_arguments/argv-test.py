# command-line arguments are values you pass to a script when you run it from the terminal

# for example:
# python lumberjack.py logs.txt --errors 10

# lumberjack.py is the script
# logs.txt is an argument
# --errors is an option/flag
# 10 is the value associated with errors

# the simplest method: sys.argv

# python exposes raw command-line arguments through sys.argv

import sys
print(sys.argv)

# Important detail: sys.argv[0] is always the script name.

filename = sys.argv[1]
print(f"Reading {filename}")

