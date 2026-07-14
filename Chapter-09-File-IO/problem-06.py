# Write a program to mine a log file and find out whether it contains ‘pythonʼ.

with open('Chapter-09-File-IO/log.txt','r') as file:
    content=file.read()
if 'python' in content.lower():
    print("File contains the word 'python'")
else:
    print("File does not contain the word 'python'")