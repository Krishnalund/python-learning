# Repeat program 4 for a list of such words to be censored.

with open('file.txt','r') as file:
    content = file.read()

words = ['Donkey' , 'Monkey', 'Cat']
for word in words:
    content = content.replace(word,'#####')

with open('file.txt','w') as file:
    file.write(content)