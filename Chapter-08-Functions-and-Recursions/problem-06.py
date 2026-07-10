# Write a python function which converts inches to cms
def inches_to_cms(inches):
    return inches * 2.54
inches=float(input('Enter number in inches: '))
result=inches_to_cms(inches)
print(f"{inches} inch = {result:.2f} cm")
