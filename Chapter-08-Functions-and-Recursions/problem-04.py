# Write a recursive function to calculate the sum of first n natural numbers
def sum_natural(n):
    if n==0:
        return 0
    else:
        return n + sum_natural(n-1)
n=int(input('Enter a number: '))
if n<0:
    print('Enter a non-negative number')
else:
    result=sum_natural(n)
    print('The sum of first',n,'natural numbers:',result)