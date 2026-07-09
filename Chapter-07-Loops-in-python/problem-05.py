# Write a program to find the sum of first n natural numbers using while loop.
n=int(input('Enter n: '))
sum_of_numbers=0
i=1
if n<=0:
    print('Invalid input')
else:
    while i<=n:
        sum_of_numbers+=i
        i+=1
    print(sum_of_numbers)