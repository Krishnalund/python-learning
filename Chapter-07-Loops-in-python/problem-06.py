# Write a program to calculate the factorial of a given number using for loop.
num=int(input('Entr a number: '))
fact=1
if num<0:
    print('Invalid input')
else:
    for i in range(1 , num+1):
        fact*=i
    print(fact)

