# sorting iterable data structures with sorted()

numbers = [5, 2, 9, 1]

result = sorted(numbers)

print(result)
print(numbers) # The original list is unchanged.

# sorting in reverse
reversed = sorted(numbers, reverse=True) # sorts in descending order

print(reversed)


# sorting with the key argument

servers = [
    ("pollux", 2),
    ("minecraft", 5),
    ("castor", 1)
]
 
print(sorted(servers)) # this just sorts by the first item in each tuple, so basically alphabetical order. 

result = sorted(servers,key=lambda item: item[1])
print(result) 
