times = [240, 103, 88]

print(sorted(times)) # this does not change the list itself, it just returns the sorted version

times.sort() # this changes the list itself
print(times)

# printing in reverse sorted order
print(sorted(times, reverse=True))


logs = [
    ("mc", 200, 42.5),
    ("web", 500, 103.2),
    ("api", 503, 88.7)
]

print(sorted(logs)) # starts comparing tuples from the beginning
# in this case, it prints in alphabetical order.

print(sorted(logs, key=lambda log: log[2]))
# looks weird, but basically means "for each log, use log[2] as its sorting value"


# combining key with reverse, we can sort by a specific value in the reverse order
print(sorted(logs, key=lambda log: log[2], reverse=True)) # essentially the reverse of the above