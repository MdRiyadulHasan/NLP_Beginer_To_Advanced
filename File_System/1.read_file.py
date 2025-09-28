# Open file in read mode
file = open("File_System/example.txt", "r")

# Read entire content
content = file.read()
print(content)

# Read line by line
file.seek(0)  # Go back to start
for line in file:
    print(line.strip())  # .strip() removes newline

# Read specific lines
file.seek(0)
print(file.readline())  # Reads first line
print(file.readlines())  # Reads all lines as a list

file.close()
