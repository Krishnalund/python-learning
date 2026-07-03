# Write a python program to print the contents of a directory using the os module. 
import os
# Specify the directory path
path = "."

# Print all files and folders in the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)