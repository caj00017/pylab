# A generator is a function that produces values one at a time, opnly when you ask for them, instead of building and returning everything at once.

# A normal function might do this:

def get_numbers():
    numbers = []

    for i in range(5):
        numbers.append(i)

    return numbers

# Then, calling

print(get_numbers())

# Gives you the whole list immediately. 


# A generator does this instead:

def generate_numbers():
    for i in range(5):
        yield i

# The key difference is 'yield' 
# When python yields i, it does three things:

    # 1. Gives that value back to whoever asked for it
    # 2. Pauses the function
    # 3. Remembers exactly where it left off. 

# Then, when you ask for another value, it resumes from that spot. 

# For example:

nums = generate_numbers()

print(nums)
print(next(nums))
print(next(nums))
print()


# Observation: This reminds me of Scanner.next() from Java. 

# One thing to note: You usually don't use next() manually. A for loop usually does it for you. 

nums = generate_numbers()

for number in nums:
    print(number)


print()

# Another important note: Generators get consumed, so if I'm done with nums, I can't use it again. 
for number in nums:
    print(number) # Note that this prints nothing, because the generator in nums is now empty, it's been iterated through already.


# Exercise
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for number in countdown(5):
    print(number) 

# Desired output: 5 4 3 2 1


# Next exercise
counter = countdown(3)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) # This one should cause a 'StopIteration' exception

