# Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
# contains the word ‘twinkleʼ.
f = open('Chapter-09-File-IO/poems.txt','r')
poem = f.read()
if 'twinkle' in poem.lower():
    print("Yes! File contains the word 'twinkle'")
else:
    print("No! File does not contain the word 'twinkle'")
f.close()
