# Write mode: creates file if it doesn't exist, overwrites if it does
file = open("File_System/example1.txt", "w")
file.write("Hello World!\n")
file.write("Python File Handling\n")
file.close()