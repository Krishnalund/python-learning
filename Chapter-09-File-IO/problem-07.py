# Write a program to find out the line number where python is present from problem-06.

with open('Chapter-09-File-IO/log.txt','r') as file:
    line_num=1
    for line in file:
        if 'python' in line.lower():
            print('python is present on line number',line_num)
        line_num+=1