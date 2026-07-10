#  Write a python function to print first n lines of the following pattern.
# ***
# **    - for n = 3
# *

def pattern(n):
    if n==1:
        print('*')
    else:   
        print('*'*n)
        pattern(n-1)
n=int(input('Enter a number: '))
if n<=0:
    print('Enter a positive integer')
else:
    pattern(n)
