# A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

with open('file.txt','r') as file:
    content = file.read()

content = content.replace('Donkey','#####')

with open('file.txt','w') as file:
    file.write(content)

