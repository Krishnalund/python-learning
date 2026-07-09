# Write a program to find whether a given number is prime or not.
num=int(input('Enter a number: '))
if num<2:
    print('It is not a prime number')
else: 
    for i in range(2,num):
        if num%i==0:
            print('Not prime number')
            break
    else:
        print('Prime number')
