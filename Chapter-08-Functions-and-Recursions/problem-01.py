#  Write a program using functions to find greatest of three numbers.
# def greatest():
#     num1=int(input('Enter first number: '))
#     num2=int(input('Enter second number: '))
#     num3=int(input('Enter third number: '))
#     largest=num1
#     if num2>largest:
#         largest=num2
#     if num3>largest:
#         largest=num3
#     print('Greatest of three numbers is:',largest)

# greatest()

def greatest(num1 , num2 , num3):
    if(num1>=num2 and num1>=num3):
        return num1
    elif(num2>=num1 and num2>=num3):
        return num2
    else:
        return num3
    
print(greatest(78,45,90))