# Write a python function to print multiplication table of a given number.
def mul_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")

num=int(input('Enter a number: '))
mul_table(num)