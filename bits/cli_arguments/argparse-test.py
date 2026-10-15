# command-line arguments are values you pass to a script when you run it from the terminal

# for example:
# python lumberjack.py logs.txt --errors 10

# lumberjack.py is the script
# logs.txt is an argument
# --errors is an option/flag
# 10 is the value associated with errors

# The better method: Argparse

# Python's standard library has a module specifically for CLI programs

import argparse

# create a parser
parser = argparse.ArgumentParser()

# add an arugment, in this case the filename
# this line defines a positional argument, which means the user has to provide it
# if they don't, python throws an error
parser.add_argument(   
    "filename",
    help="Log file to analyze" # A help value can be provided for when the user uses -h
)

# optional arguments

# we can also create arguments like:
# --limit 10

# parser.add_argument("--limit", type=int)

# and we can provide defaults, wbhich means the user does not have to specify this flag
# if the user does specify, the default gets overwritten
parser.add_argument(
    "-n", # can provide a short flag version
    "--limit", # or a long one
    type=int,
    default=10,
    help="Maximum number of results to display"
)

# boolean flags
# say we want --verbose, but dont want the user to type '--verbose true'

parser.add_argument(
    "-v", # can provide a short flag version
    "--verbose", # or a long one
    action="store_true"
)


# use the parser to parse out the args
args = parser.parse_args()

print(f"Filename: {args.filename}")
print(f"Limit: {args.limit}")
print(f"Verbose?: {args.verbose}")

