# File I/O
# Modes for opening a file include:
# w - Writing
# r - Reading
# a - Append to the end
# x - Create a new file, fail if it already exists.

with open("logs.txt", "r", encoding="utf-8") as file: # optionally, you can explicitly specify UTF-8
    lines = []
    for line in file: # the file is iterable by lines
        lines.append(line)
        # print(line) # prints out each line in the file with spaces between them (because each line has a newline at the end of it)
        print(line.strip()) # strips out the whitespace between each line

    contents = file.read() # this read method will return the complete contents of the file (as what?)

with open("report.txt", "w") as file:
    file.write("HOMELAB HEALTH REPORT\n")
    file.write("Everything is on fire.\n")

with open("report.txt", "a") as file:
    file.write("New warning detected\n")

print(contents) # Note that this doesn't print out anything. Look at where file.read() takes place above. We've already consumed the entire file with "for line in file"
# A file object keeps track of its current position. After the loop finishes, the cursor is at the end of the file, so file.read() returns an empty string. 
# I'm leaving this here as a good example of something going wrong, but if I wanted to iterate through the complete file and then reset it so I can use file.read(),
# then I would use file.seek(0) before I use file.read(). file.seek(0) will move the cursor back to the beginning of the file. 

# I hypothesize that file.seek() will move the cursor to any line in the file that I want it to. I'm going to give it a try.

with open("logs.txt", "r") as file:
    file.seek(5)
    print(file.read())

# Interesting, so file.seek() seems to specify the INDEX of the content to start at (including the char at that index), not the LINE NUMBER. 
# I looked it up and specifically, this is a byte offset, not an "index" or "character" really, though it seems to function similarly. 