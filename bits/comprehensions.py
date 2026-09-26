import os

### list comprehensions

# let's say i want to square every number in this list

numbers = [1,2,3,4,5]

squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)

# alterantively, i can compress this into a comprehension. 

squares = []

squares = [num ** 2 for num in numbers]

print(squares)

# The basic pattern is: [expression for item in iterable] 

# Therefore,

names = ["alice", "bob", "charlie"]
uppercase = [name.upper() for name in names] # Note that the left side is what gets placed into the new list

print(uppercase)


# Filtering while constructing

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

# The above is equivalent to the below

evens = [num for num in numbers if num % 2 == 0]
# [expression for item in iterable if condition]; in the case above, we just put num, but we could perform operations on it if we wanted, as shown below

squares_of_evens = [
    num ** 2
    for num in numbers
    if num % 2 == 0
]

# basically this converts to:
# squares_of_evens = []
# for num in numbers:
#     if num % 2 == 0:
#         squares_of_evens.append(num ** 2)

print(squares_of_evens)


### Set comprehensions

numbers = [1,2,2,3,3,3,4]
unique_squares = {num ** 2 for num in numbers} # note the braces rather than brackets, remember that this is set notation

print(f"Unique squares: {unique_squares}")
# Once again the pattern is {expression for item in iterable}

# Note that sets remove duplicates, this is useful for something like logs.

services = [
    "nginx",
    "ssh",
    "nginx",
    "postgres",
    "ssh"
]

unique_services = {service for service in services}
print(unique_services)

long_names = {
    service
    for service in services
    if len(service) > 3
}

print(long_names)


### Dict comprehensions
# These look slightly different because every dictionary entry needs a key and a value

squares = {}

for num in numbers:
    squares[num] = num ** 2

# The following is equivalent to the above

squares = {num: num ** 2 for num in numbers}
# Pattern: {key_expression: value_expression for item in iterable}

services = ["nginx", "ssh", "postgres"]
name_lengths = {
    service: len(service)
    for service in services
}
print(name_lengths)

long_services = {
    service: len(service)
    for service in services
    if len(service) > 3
}
print(long_services)

os.system("clear")

### List Exercises

response_times = [120,450,80,900,200,610]

# Write one list comprehension that creates a list containing only response times greater than 300
long_response_times = [time for time in response_times if time > 300]
print(long_response_times)


# Write a list comprehension that keeps only response times greater than 300 and coverts those times from ms to seconds by dividing by 10000
long_response_times_seconds = [time/1000 for time in response_times if time > 300]
print(long_response_times_seconds)


### Set Exercises

services = ["nginx", "ssh", "nginx", "postgres", "ssh", "redis"]

# Write a set comprehension that keeps only service names longer than 3 characters
long_services = {service for service in services if len(service) > 3}
print(long_services)


### Dict Exercises

services = ["nginx", "ssh", "postgres", "redis"]

# Create a dictionary using comprehensions where each service name is the key, its length is the value and only include services longer than 3 characters

long_service_lengths = {
    service: len(service)
    for service in services
    if len(service) > 3
}

print(long_service_lengths)

# Given:

services = ["nginx", "ssh", "postgres", "redis"]

# Create a dictionary where the key is the service name in uppercase, the value is the length of the original service name and only include services with length at least 5

service_names_upper_long = {
    service.upper(): len(service)
    for service in services
    if len(service) >= 5
}

print(service_names_upper_long)


### GENERAL EXERCISES

logs = [
    ("nginx", 200),
    ("ssh", 500),
    ("postgres", 503),
    ("redis", 200),
    ("nginx", 404)
]

# create a set comprehension containing the names of services whose status code is 400 or higher
errors = {
    log[0] 
    for log in logs
    if log[1] >= 400
}
print(errors)