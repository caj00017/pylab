# While looping, what information do I need besides the current item?

services = ["nginx", "redis", "minecraft"]

for service in services:
    print(service) 

# Python gives us each item directly, we don't need to reach for indexes unless we actually need them

### Enumeration: "I need the item AND its position"

# NOTE: This code is very Java. Instead of doing this, we should use enumerate()
for i in range(len(services)):
    print(i, services[i])

# Python usually prefers:

for i, service in enumerate(services): # Note that this is already tuple unpacking, which I'll revisit later. 
    print(i, service)

for i, service in enumerate(services, start=1): # can also specify a start value
    print(i, service)

# Mental rule: Use enumerate() when youn care about both the elemtn and its index.

# Small exercise. Given:

hosts = ["pollux", "castor", "pi"]

# Write a loop that prints:
# Host 1: pollux
# Host 2: castor
# Host 3: pi

for i, host in enumerate(hosts, start=1):
    print(f"Host {i}: {host}")

# zip() - "I want to walk through multiple collections together" 

hosts = ["pollux", "castor", "pi"]
temperatures = [52.1, 47.8, 61.0]

# I could awkwardly do:
for i in range(len(hosts)):
    print(hosts[i], temperatures[i])

# But Python gives us zip():
for host, temperature in zip(hosts, temperatures):
    print(host, temperature)

# Conceptually, zip() pairs things up like:
# ("pollux", 52.1)
# ("castor", 47.8)
# ("pi", 61.0)
# Then host, temperature unpacks each pair. 
# One important detial: zip() stops when the shortest iterable runs out
# I was wondering what happens if one list is longer. 

temperatures = [52.1, 47.8]

print("Short list:")
for host, temperature in zip(hosts, temperatures):
    print(host, temperature)

# Mental rule: Use zip() when corresponding items in multiple collections belong together. 

### Tuple unpacking - very Pythonic and extremely important. 
# I've already gone over this but a review never hurts. 

measurement = ("pollux", "cpu", 72.5)

# I could do the following:
host = measurement[0]
metric = measurement[1]
value = measurement[2]

# But Python lets me unpack it like this:
host, metric, value = measurement
print(host, metric, value)

# note that i cannot unpack fewer values than there are
# host, metric = measurement; would be invalid
# instead, if i don't care about a value, i can just do

host, metric, _ = measurement

# I learned this from Go but apparently it's a very Python trick as well. 

# Another good thing to know, you can swap two variables like

first = 1
second = 2
first, second = second, first 
print(first, second) # should print 2, 1

# No temporary variable needed. 

### range() - generate integers

# This is the one that Java programmers usually use

for i in range(5):
    print(i)

# Range 5 means start at 0, stop before 5
# there are three forms:
# range(stop)
# range(start, stop)
# range(start, stop, step)

print()

for i in range(2, 6):
    print(i)

print()

for i in range(0, 10, 2):
    print(i)


# Use range() when numbers themselves mater, such as:
# for attempt in range(3):
# or 
# for port in range(8000, 8010):


### Iterating dictionaries correctly.

metrics = {
    "pollux": 72.5,
    "castor": 61.2,
    "pi": 83.4
}

# Iterating over keys

for thing in metrics:
    print(thing)

# Which is equivalent to:

for host in metrics.keys():
    print(host)


# Although the first version is generally cleaner
# If I only need values:

for value in metrics.values():
    print(value)

# and if i need both i can just do:

for host, value in metrics.items():
    print(host, value)

# so, keys() returns a list of my keys, values() returns a list of my values, and items() returns a list of tuples with my keys and values both


### Putting multiple idioms together. Consider:

metrics = {
    "pollux": 72.5,
    "castor": 61.2,
    "pi": 83.4
}

for number, (host, value) in enumerate(metrics.items(), start=1):
    print(number, host, value)

# Before I run this, let me try and figure out what this is going to do. 
# First, it's going to give me a list of tuples containing each key value pair from metrics,
# Then it's going to enumerate them starting at one, and return to me the number of the particular tuple
# as well as the host and value from metrics.items(). i believe there's a nested tuple here. 
# i think my output is going to look something like:
# 1 pollux 72.5
# 2 castor 61.2
# 3 pi 83.4

# Bingo!

### So to review,

# If I need just the items -> for item in things
# if i need each item and its index -> for i, thing in enumerate(things)
# if i need corresponding items from two collections -> for a_thing, b_thing in zip(a, b)
# if i need a sequence of numbers -> for i in range(...)
# if i'm iterating a dictionary ->
    # keys only -> for key in dictionary
    # values only -> for value in dictionary.values()
    # both -> for key, value in dictionary.items()